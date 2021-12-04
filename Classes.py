from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Player:

    def __init__(self, bank):
        self.bank = bank

        self.hand = []

    def get_funds(self):
        return self.bank

    def add_card_to_hand(self, card):
        self.hand.append(card)


class Dealer:

    def __init__(self):
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        self.value = values[self.rank]

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)


class Table:

    def __init__(self):
        self.total_bets = 0

    def add_to_bets(self, bet):
        self.total_bets = self.total_bets + bet

    def get_bets(self):
        return self.total_bets

    def reset_bets(self):
        self.total_bets = 0
