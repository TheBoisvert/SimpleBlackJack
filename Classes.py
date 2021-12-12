from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
          'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Player:
    """
    Groups everything that has to do with the player.
    """

    def __init__(self, bank):
        """
        :param bank: an int between 2 and 1000000 indicating the player's starting chip count.

        self.bank: the player's current chip count.
        self.hand: the player's current cards, initiates as an empty list
        """
        self.bank = bank

        self.hand = []
        self.bets = 0

    def add_funds(self, chips):
        """
        Adds chips to the player's bank

        :param chips: an amount of chips to add to the bank
        :return: none
        """

        self.bank = self.bank + chips

    def get_funds(self):
        """
        A simple method used to get the player's current chip count.

        :return: the value of self.bank
        """

        return self.bank

    def add_card_to_hand(self, card):
        """
        A simple method to add a card the player's current hand.

        :param card: a Card object
        :return: none
        """

        self.hand.append(card)

    def remove_cards_from_hand(self):
        """
        Removes every card from the player's hand.

        :return: none
        """

        self.hand = []

    def add_to_bets(self, bet):
        """
        Withdraws the bet amount from the player bank.
        Adds the bet amount to the player current bets.

        :param bet: an int representing a chip amount
        :return: none
        """

        self.bank = self.bank - bet
        self.bets = self.bets + bet

    def get_bets(self):
        """
        A simple method to get the current bet amount

        :return: the player's current bet amount.
        """

        return self.bets

    def reset_bets(self):
        """
        A simple method to reset the bet count to 0

        :return: none
        """

        self.bets = 0


class Dealer:
    """
    Groups everything that has to do with the dealer.
    """

    def __init__(self):
        """
        self.hand: the player's current cards, initiates as an empty list
        """

        self.hand = []

    def add_card_to_hand(self, card):
        """
        A simple method to add a card the player's current hand.

        :param card: a Card object
        :return: none
        """

        self.hand.append(card)

    def remove_cards_from_hand(self):
        """
        Removes every cards from the dealer's hand.

        :return: none
        """

        self.hand = []


class Card:
    """
    Groups everything that has to do with cards.
    """

    def __init__(self, suit, rank):
        """
        :param suit: one of either 4 possible card suit ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        :param rank: one of either 13 possible card rank ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

        self.suit: the card's suit
        self.rank: the card's rank
        self.value: the card's value
        """

        self.suit = suit
        self.rank = rank

        self.value = values[self.rank]

    def __str__(self):
        """
        A simple method to know the current card's suit and rank

        :return: a formatted string indicating the card's suit and rank
        """
        return "{} of {} --> {}".format(self.rank, self.suit, self.value)


class Deck:
    """
    Groups everything that has to do with the dealer.
    """

    def __init__(self):
        """
        self.deck: the current states of the deck, initiates as a complete 52 cards deck
        """

        self.deck = []

        # Creates every possible cards and appends them to self.deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        """
        A simple method used to shuffle de deck of cards

        :return: none
        """

        shuffle(self.deck)

    def draw_card(self):
        """
        A simple method to draw a card from the deck.

        :return: the card on top of the deck
        """

        return self.deck.pop(0)

    def add_card(self, card):
        """
        A simple method to add a card to the deck.
        Used at the end of a round to add the player's and dealer's cards back into the deck

        :param card: a card object
        :return: none
        """

        self.deck.append(card)
