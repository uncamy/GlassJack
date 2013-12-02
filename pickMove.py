# determine which card you should play
import readCard
#import theBook

#returned from cardReader --> card 1 and card 2
test_ace =[('A', 'S', 'A'), ('J', 'H', '10'), ('3', 'H', '3')]

#consider adding a turn count this is addequate for all game states
def whos_card(cards):
    if len(cards) <5:
        player_hand = cards[:2]
        dealer_hand = cards[3]
    else:
        player_hand = cards[:3]
        dealer_hand = cards[2:]

def score(card1, card2):


if (card1 or card2 == 'A'):
        hand = (card1 + card2)
        my_hand = (','.join(hand))
    else:
        my_hand = int(card1) + int(card2)

    return my_hand


def main():
  cards = readCard.main()
  card_value = [x[2] for x in cards]
  check4ace= map(score, card_value)

'''
1. we need to processs the card to make sure they are in the right form
2. search the dictionary for that pair
3. return the correct move (H, D, S, P)
'''
