Glass Jack
========================
Glass Jack is a Black Jack card reader for Google Glass. The app identifies the cards currently being played by the dealer and the Glass Jack player and suggests a move (hit, stay, double down). This is a project in progress. Interested? Contact me to collaborate on this project! 

<h4>How it Works</h4>
This game uses Open CV for the image processing, and Google's Mirror API for Glass. I used the Python quickstart for the mirror api. Please see here for more information: https://developers.google.com/glass/quickstart/python. The image processing is based heavily on the work by Arnab Nandi https://github.com/arnabdotorg/Playing-Card-Recognition. As with his project, we are using a very simple image processing algorithm that is not robust, however, it does process quickly. The fast processing speeds are needed for real time play, and the simple algorithm for card recognition will be sufficient for this protoype.

<h4>Status</h4>
<strong>Working!</strong><br/>
- Card reader<br/>
- Card scoring<br/>
- Connecting to Glass</br>
- Receiving images from Glass<br/>

<strong>In Progress</strong>
- Calculate move
- Formatting cards
- Sending response to Glass

