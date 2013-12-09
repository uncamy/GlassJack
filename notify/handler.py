# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Request Handler for /notify endpoint."""

__author__ = 'alainv@google.com (Alain Vongsouvanh)'


import io
import json
import logging
import webapp2

from apiclient.http import MediaIoBaseUpload
from oauth2client.appengine import StorageByKeyName

from model import Credentials
import util


def send_to_file():
  im = open('attachment.txt', 'wb')
  im.write ('writing stuff')
  im.close()

class NotifyHandler(webapp2.RequestHandler):
  """Request Handler for notification pings."""


  def post(self):
    """Handles notification pings."""
    logging.info('Got a notification with payload %s', self.request.body)
    data = json.loads(self.request.body)
    userid = data['userToken']
    # TODO: Check that the userToken is a valid userToken.
    self.mirror_service = util.create_service(
        'mirror', 'v1',
        StorageByKeyName(Credentials, userid, 'credentials').get())
    if data.get('collection') == 'locations':
      self._handle_locations_notification(data)
    elif data.get('collection') == 'timeline':
      self._handle_timeline_notification(data)



  def _handle_timeline_notification(self, data):
    """Handle timeline notification."""
    for user_action in data.get('userActions', []):
      if user_action.get('type') == 'SHARE':
        # Fetch the timeline item.
        item = self.mirror_service.timeline().get(id=data['itemId']).execute()
        attachments = item.get('attachments', [])
        media = None
        if attachments:
          # Get the first attachment on that timeline item and do stuff with it.
          attachment = self.mirror_service.timeline().attachments().get(
              itemId=data['itemId'],
              attachmentId=attachments[0]['id']).execute()
          resp, content = self.mirror_service._http.request(
              attachment['contentUrl'])


          if resp.status == 200:
            media = MediaIoBaseUpload(
                io.BytesIO(content), attachment['contentType'],
                resumable=True)
          else:
            logging.info('Unable to retrieve attachment: %s', resp.status)
        body = {
          # "html": "<article style=\"left: 0px; visibility: visible;\">\n
          #    <section>\n
          #      <div class=\"layout-two-column\">\n
          #         <div class=\"align-center\">\n
          #           <p> </p>\n
          #           <p class=\"text-large\"> you: A5</p>\n
          #           <p class=\"text-large\"> dealer: 7 \n </p>
          #         </div>\n
          #         <div class=\"align-center\">\n
          #            <br>\n
          #            <p class=\"text-x-large\">HIT!</p>\n
          #         </div>\n
          #      </div>\n
          #     </section>\n
          #    <footer>\n
          #       <p>Glass Jack</p>\n
          #    </footer>\n</article>",
          "text": "Glass Jack is processing your image",
          "notification": {
             "level": "DEFAULT"
          }
        }

        self.mirror_service.timeline().insert(
            body=body, media_body=media).execute()

        # Only handle the first successful action.
        break
      else:
        logging.info(
            "I don't know what to do with this notification: %s", user_action)

  def download_attachments(self, attachment):
    resp, content = service._http.request(attachment['contentUrl'])
    if resp.status == 200:
      return content
    else:
      print 'An error occurred: %s' % resp
      return None

NOTIFY_ROUTES = [
    ('/notify', NotifyHandler)
]
