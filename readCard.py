# This file uses image recognition to identify the cards that are currently on the table
import cv2
import sys
import numpy as np


#numcards = 56

#im =cv2.imread('twoCards.png')
#im =cv2.imread('glass_example.png')
#im =cv2.imread('card_example.png')
#im =cv2.imread('training_cards.png')
#im =cv2.imread('glass_training_deck.png')

#Image matching
def rectify(h):
    h = h.reshape((4,2,))
    hnew = np.zeros((4,2), dtype = np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]
    return hnew

def preprocess(im):
    """preporcess to remove artifacts"""
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1,1), 1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)
    return thresh

def imgdiff(im1, im2):
    im1 = cv2.GaussianBlur(im1, (5,5),5)
    im2 = cv2.GaussianBlur(im2, (5,5),5)
    diff = cv2.absdiff(im1, im2)
    diff = cv2.GaussianBlur(diff, (5,5),5)
    flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY)
    return np.sum(diff)

def find_closest_card(training, im):
    features = preprocess(im)
    return sorted(training.values(), key=lambda x:imgdiff(x[1], features))[0][0]

#Getting cards
def getCards(im, numcards=4):
    """remove artifacts"""
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1,1), 1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

    #find the contours
    contours, hierarchy =cv2.findContours(thresh, cv2.RETR_TREE,\
                            cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key= cv2.contourArea, reverse =True) [:numcards]

    for card in contours:
        peri = cv2.arcLength(card, True)
        approx = rectify(cv2.approxPolyDP(card, 0.02*peri, True))
        h = np.array([ [0,0],[449,0],[449,449],[0,449] ],np.float32)
        transform = cv2.getPerspectiveTransform(approx,h)
        warp =cv2.warpPerspective(im, transform, (450, 450))

        yield warp

    #contour_im = cv2.drawContours(im, contours,  -1, (0,255,0),3)
def get_training(training_labels_filename, training_image_filename,\
                 num_training_cards, avoid_cards = None):
    training = {}

    labels = {}
    for line in file(training_labels_filename):
        key, num, suit, score = line.strip().split()
        labels[int(key)] = (num, suit, score)

    print "Training"

    im = cv2.imread(training_image_filename)
    for i, c in enumerate(getCards(im, num_training_cards)):
        if avoid_cards is None or (labels[i][0] not in avoid_cards[0] and\
                                   labels[i][1] not in avoid_cards[1]):
            training[i] = (labels[i], preprocess(c))
    print "Done Training"
    return training

def main():
    filename = sys.argv[1]
    training_image_filename = sys.argv[2]
    training_labels_filename = sys.argv[3]
    num_cards = 4
    num_training_cards = 56

    training = get_training(training_labels_filename,\
                                training_image_filename, num_training_cards)
    im = cv2.imread(filename)
    width = im.shape[0]
    height = im.shape[1]
    if width < height:
        im = cv2.transpose(im)
        im = cv2.flip(im, 1)

    cards = [find_closest_card(training, c) for c in getCards(im, num_cards)]
    print cards


main()

#display image
def display_image(image):
    """displays image in the python REPL"""
    cv2.namedWindow('Display Window')
    cv2.imshow('Display Window', image)




#display_image(im)
