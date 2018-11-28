class card:
    def _init_(self, suit, value):
        self.suit = suit
        self.value = value

'''
Suits:
Spades = 1
Hearts = 2
Clubs = 3
Diamonds = 4

Values:
Two = 2
...
Jack = 11
Queen = 12
King = 13
Ace = 14 (to preserve showdown value order - i.e. Ace > King)
'''
class hand:
    def _init_(self, card1, card2):
        self.cards = [card1, card2]

class range:
    def _init_(self, hands):
        self.hands = hands