# This file uses image recognition to identify the cards that are currently on the table
import cv2
import numpy as np


numcards = 56

#im =cv2.imread('twoCards.png')
#im =cv2.imread('glass_example.png')
#im =cv2.imread('card_example.png')
im =cv2.imread('training_cards.png')
#im =cv2.imread('glass_training_deck.png')

#preporcess to remove artifacts
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (1,1), 1000)
flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

#find the contours
contours, hierarchy =cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key= cv2.contourArea, reverse =True) [:numcards]
contour_img = cv2.drawContours(im, contours,  -1, (0,255,0),3)

#display image
def display_image(image):
    """displays image in the python REPL"""
    cv2.namedWindow('Display Window')
    cv2.imshow('Display Window', im)

def process_image(numcards):
    for i in range(numcards):
        card = contours[i]
        peri = cv2.arcLength(card, True)
        approx = np.array((cv2.approxPolyDP(card, 0.02*peri, True)), np.float32)
        rect = cv2.minAreaRect(contours[i])
        r = cv2.cv.BoxPoints(rect)
        h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
        transform = cv2.getPerspectiveTransform(approx,h)
        warp =cv2.warpPerspective(im, transform, (450, 450))

display_image(im)


