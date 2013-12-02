# determine which card you should play
import readCard
#import theBook

#returned from cardReader --> card 1 and card 2
test_ace =[('A', 'S', 'A'), ('J', 'H', '10'), ('3', 'H', '3')]

#consider adding a turn count. this is not adequate for all game states
def whos_card(cards):
    if len(cards) <5:
        player_hand = cards[:2]
        dealer_hand = cards[2:]
    else:
        player_hand = cards[:3]
        dealer_hand = cards[2:]
    print 'Player\'s Hand is: %s' % player_hand
    print 'Dealer\'s Hand is: %s' % dealer_hand
    return player_hand, dealer_hand

def score(hand):
    if len(hand) > 1:
        if hand[0][0] == hand[0][1]:
            print 'We have two matching cards'
            return hand
        elif hand[0][0] == 'A' or hand[0][1] == 'A':
            print 'We have an Ace!'
            return hand
        else:
            sum_hand = str(int(hand[0][0]) + int(hand[0][1]))
            print 'We have a score of %s' %sum_hand
            return sum_hand

def main():
  cards = readCard.main()
  card_value = [x[2] for x in cards]
  card_owner = whos_card(card_value)
  score(card_owner)

  check4ace= map(score, card_value)

'''
1. we need to processs the card to make sure they are in the right form
2. search the dictionary for that pair
3. return the correct move (H, D, S, P)
'''
