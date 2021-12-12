from Classes import *


def starting_chip_count():
    """
    Establishes the players starting chip count
    :return: The player's initial chip count
    """

    while True:
        print("How many chips would you like to play with?")
        bank = input()

        if not bank.isnumeric():
            # This also filters out float such as 40.5 or 100.333
            print("This is not a valid chip count.")
            continue
        elif bank.isnumeric() and int(bank) == 0:
            print("You cannot play with 0 chips.")
            continue
        elif bank.isnumeric() and int(bank) < 2:
            print("You cannot play with less than 2 chips.")
            continue
        elif bank.isnumeric() and int(bank) > 1000000:
            print("You cannot play with more than 1,000,000 chips.")
            continue
        else:
            break

    return int(bank)


def start_of_turn():
    """
    The game/round officially starts here
    Will continue running until the player doesn't want to play anymore, or is out of funds.
    """

    # Clears the terminal
    print("\n" * 100)

    # Checks if the player has enough funds to play this round
    check_funds()

    # Asks the player to place a bet for this round
    place_bet()

    # Deals the player and dealer each 2 cards from the shuffled deck
    player.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())
    player.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())

    # Prints out the current state of the game
    print("\n" + "The Dealer's hand :")
    for card in dealer.hand:
        if card == dealer.hand[-1]:
            print("~~~")
        else:
            print(card)

    print("\n" + "Your hand :")
    for card in player.hand:
        print(card)

    check_blackjack()

    deal_or_stand()


def check_funds():
    """
    Checks if the player has enough funds to play the round
    Exits the game if the player's chip count is below 2, which is the minimum amount to place a bet.

    :return: none
    """

    if player.get_funds() < 2:
        print("You cannot play with less than 2 chips in your bank!")
        print("Better luck next time!")
        exit()
    else:
        return


def place_bet():
    """
    Asks the player to place a bet at the beginning of the current round

    :return: none
    """

    while True:
        print("Place your bet!")
        bet = input()

        if not bet.isnumeric():
            # This also filters out float such as 40.5 or 100.333
            print("This is not a valid chip count.")
            continue
        elif int(bet) > player.get_funds():
            print("You cannot bet more chips than what you have in your bank!")
            continue
        elif int(bet) < 2:
            print("You cannot bet less than 2 chips!")
            continue
        elif int(bet) > 500:
            print("You cannot bet more than 500 chips!")
            continue
        else:
            break

    player.add_to_bets(int(bet))


def check_blackjack():
    """
    Checks if the player has a "blackjack", meaning exact 21 card value in his hand

    :return: none
    """

    player_hand_value = 0
    dealer_hand_value = 0
    for card in player.hand:
        player_hand_value = player_hand_value + card.value
    for card in dealer.hand:
        dealer_hand_value = dealer_hand_value + card.value

    if player_hand_value == 21 and dealer_hand_value != 21:
        blackjack()


def blackjack():
    """
    If this method is called, the player has a blackjack while the dealer does not and wins the round!

    :return: none
    """

    print("Congratulation! You win the round!")
    print("You have a blackjack and the dealer hasn't!")

    # Pays the player 3 to 2
    winnings = round(player.get_bets() * 1.5)
    print("You bet a total of {} chips, you then win {} chips!".format(player.get_bets(), winnings))
    player.add_funds(winnings)
    print("you now have a total of {} chips!".format(player.get_funds()))

    # Asks the player if he wants to play again
    expected = ["Y", "N", "y", "n"]
    while True:
        play_again = input("Would you like to play another round? (Y / N) : ")

        if play_again not in expected:
            print("This is not a valid choice!")
            continue
        else:
            if play_again == "Y" or play_again == "y":
                break
            else:
                exit()

    # Removes the cards from the player's and dealer's hand, and puts then back in the deck
    for card in player.hand:
        current_card = player.remove_card_from_hand()
        deck.add_card(current_card)
    for card in dealer.hand:
        current_card = dealer.remove_card_from_hand()
        deck.add_card(current_card)

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def deal_or_stand():
    """
    Asks the player if he wants another card, or if he wants to stand (keep the card he currently has in hand).

    :return: none
    """

    expected = ["DEAL", "Deal", "deal", "STAND", "Stand", "stand"]

    while True:
        deal_stand = input("Would you like to be dealt another card or stand on your current cards? "
                           "(deal / stand) : ")

        if deal_stand not in expected:
            print("This is not a valid choice!")
            continue
        else:
            if deal_stand == "DEAL" or deal_stand == "Deal" or deal_stand == "deal":
                player.add_card_to_hand(deck.draw_card())

                print("\n" + "Your hand :")
                for card in player.hand:
                    print(card)

                check_bust()

                continue
            else:
                return


def check_bust():
    """
    Checks if the player has gone "bust".

    :return: none
    """

    # TODO: how to deal with aces?

    player_hand_value = 0

    for card in player.hand():
        player_hand_value = player_hand_value + card.value

    if player_hand_value > 21:
        bust()
    else:
        return


def bust():
    """
    If this method is called, the player has gone "bust" and loses the round!

    :return: none
    """

    print("You've gone bust!")

    # Player loses all his bet money
    print("You bet a total of {} chips, you lost everything!".format(player.get_bets()))

    # Checks if the player has enough funds to play another round
    check_funds()

    # Asks the player if he wants to play again
    expected = ["Y", "N", "y", "n"]
    while True:
        play_again = input("Would you like to play another round?")

        if play_again not in expected:
            print("This is not a valid choice!")
            continue
        else:
            if play_again == "Y" or play_again == "y":
                break
            else:
                exit()

    # Removes the cards from the player's and dealer's hand, and puts then back in the deck
    for card in player.hand:
        current_card = player.remove_card_from_hand()
        deck.add_card(current_card)
    for card in dealer.hand:
        current_card = dealer.remove_card_from_hand()
        deck.add_card(current_card)

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


if __name__ == "__main__":
    # Initiates the player and dealer objects
    player = Player(starting_chip_count())
    dealer = Dealer()

    # Creates a single deck and shuffles it
    deck = Deck()
    deck.shuffle_deck()

    # This starts the game
    start_of_turn()
