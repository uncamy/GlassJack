# determine which card you should play
import readCard
from theBook import card_book

#returned from cardReader --> card 1 and card 2
test_ace =[('A', 'S', 'A'), ('J', 'H', '10'), ('3', 'H', '3')]
test_pair =[('7', 'S', '7'), ('7', 'H', '7'), ('3', 'H', '3')]

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

#refactor such that formatting doesn't need to be repeated for each case
def score(hand):
    if len(hand) > 1:
        if hand[0][0] == hand[0][1]:
            print 'We have two matching cards'
            player_hand = ('%s,%s') %(hand[0][0], hand[0][1])
        elif hand[0][0] == 'A':
            print 'We have an Ace!'
            player_hand = ('A,%s') %(hand[0][1])
        elif hand[0][1] == 'A':
            print 'We have an Ace!'
            player_hand = ('A,%s') %(hand[0][0])
        else:
            player_hand = str(int(hand[0][0]) + int(hand[0][1]))
    print 'Your hand is %s' %player_hand

    dealer_hand = ('%s') %hand[1][0]
    print 'The dealer\'s hand is %s' %dealer_hand

    score_round = (player_hand, dealer_hand)
    print score_round
    return score_round

def pick_move(score):
    #match book to score re.match
    mv  = card_book.get(score)
    if mv == 'H':
        move = 'Hit!'
    elif mv == 'D':
        move = 'Double Down!'
    elif mv == 'S':
        move = 'Stand'
    else:
        move = 'Split'
    return move

def game_main():
  cards = readCard.main()
  card_value = [x[2] for x in cards]
  card_owner = whos_card(card_value)
  scored = score(card_owner)
  move= pick_move(scored)
  print move
  return move

'''
1. we need to processs the card to make sure they are in the right form
2. search the dictionary for that pair
3. return the correct move (H, D, S, P)
'''
