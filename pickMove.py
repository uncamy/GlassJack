# determine which card you should play
#import cardReader
#import theBook

#reutrned from cardReader --> card 1 and card 2
def process_card(card):
    if card == 'A':
        return 'A'
    elif card == 10:
        return 10
    else:
        return card

def score(card1, card2):
    if (card1 or card2 == 'A'):
        hand = (card1 + card2)
        my_hand = (','.join(hand))
    else:
        my_hand = int(card1) + int(card2)

    return my_hand

def test1():
    card1 = 'A'
    card2 = 2

'''
1. we need to processs the card to make sure they are in the right form
2. search the dictionary for that pair
3. return the correct move (H, D, S, P)
''''
