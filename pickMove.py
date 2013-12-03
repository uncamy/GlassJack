# determine which card you should play
import readCard
from theBook import card_book

#returned from cardReader --> card 1 and card 2
test_ace =[('A', 'S', 'A'), ('J', 'H', '10'), ('3', 'H', '3')]
test_pair =[('7', 'S', '7'), ('7', 'H', '7'), ('3', 'H', '3')]

#refactor such that formatting doesn't need to be repeated for each case
def score(cards):
    assert len(cards) == 3
    dealer_value = cards.pop()
    player_hand = cards

    if 'A' in player_hand:
        print 'We have an Ace!'
        player_hand.sort(reverse=True) # move Ace to first spot
    elif player_hand[0] != player_hand[1]: # don't add doubles
        player_hand = str(sum(int(card) for card in player_hand))

    player_hand = ",".join(player_hand)
    print 'Your hand is %s' %player_hand

    print "The dealer's hand is %s" %dealer_value

    score_round = (player_hand, dealer_value)
    print score_round
    return score_round

def pick_move(score):
    #match book to score re.match
    move_choice = {'H': 'Hit!', 'D': 'Double Down!', 'S': 'Stand', 'P': 'Split'}
    return move_choice[card_book.get(score)]

def game_main():
  cards = readCard.main()
  card_value = [x[2] for x in cards]
  scored = score(card_value)
  move= pick_move(scored)
  print move
  return move

'''
1. we need to processs the card to make sure they are in the right form
2. search the dictionary for that pair
3. return the correct move (H, D, S, P)
'''
