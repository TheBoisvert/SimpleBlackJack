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
        # Starting chip count cannot be 0
        elif bank.isnumeric() and int(bank) == 0:
            print("You cannot play with 0 chips.")
            continue
        # Starting chip count cannot be less than 2, since minimum bet is 2
        elif bank.isnumeric() and int(bank) < 2:
            print("You cannot play with less than 2 chips.")
            continue
        # Starting chip count cannot be more than 1000000, eat the rich
        elif bank.isnumeric() and int(bank) > 1000000:
            print("You cannot play with more than 1,000,000 chips.")
            continue
        else:
            break

    return int(bank)


def draw_board(reveal_dealer_hand_value):
    """
    Draws the board in the terminal

    :param reveal_dealer_hand_value: a bool that indicated if we need to reveal the dealer's hand value or not
    :return: none
    """

    # Clears the board
    print("\n" * 100)

    # Prints the board
    if reveal_dealer_hand_value:
        print("\n" + "The Dealer's hand : {}".format(dealer.get_hand_value()))

        for card in dealer.hand:
            print(card)
    else:
        print("\n" + "The Dealer's hand :")

        for card in dealer.hand:
            if card == dealer.hand[-1]:
                print("~~~")
            else:
                print(card)

    print("\n" + "Your hand : {}".format(player.get_hand_value()))
    for card in player.hand:
        print(card)
    print("")


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
    draw_board(False)

    # Checks if the player has blackjack
    check_blackjack()

    # Asks the player if he wants to hit or stand
    hit_or_stand()

    # When the player is done, it's the dealer's turn
    dealer_hit_or_stand()


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
        # The player cannot bet more than the amount of chips in his bank
        elif int(bet) > player.get_funds():
            print("You cannot bet more chips than what you have in your bank!")
            continue
        # The minimum bet is 2
        elif int(bet) < 2:
            print("You cannot bet less than 2 chips!")
            continue
        # The maximum bet is 500
        elif int(bet) > 500:
            print("You cannot bet more than 500 chips!")
            continue
        else:
            break

    player.add_to_bets(int(bet))


def hit_or_stand():
    """
    Asks the player if he wants another card, or if he wants to stand (keep the card he currently has in hand).

    :return: none
    """

    expected = ["HIT", "Hit", "hit", "STAND", "Stand", "stand"]

    while True:
        hit_stand = input("Would you like to be dealt another card or stand on your current cards? "
                          "(Hit / Stand) : ")

        if hit_stand not in expected:
            print("This is not a valid choice!")
            continue
        else:
            # If the player chooses to hit, we add a card to his hand and refresh the board
            if hit_stand == "HIT" or hit_stand == "Hit" or hit_stand == "hit":
                player.add_card_to_hand(deck.draw_card())

                draw_board(False)

                # We then check for blackjack and busts
                check_blackjack()
                check_bust()

                continue
            else:
                return


def dealer_hit_or_stand():
    """
    Does the dealer's actions until either :
    - his total hand value is above the total hand value of the player
    - his hand value is 17 or more
    - he gets a blackjack
    - he busts

    :return: none
    """

    while True:
        # Don't bother checking the other options if the dealer busts
        if dealer.get_hand_value() > 21:
            bust_dealer()
        # If the player's hand value is greater than that of the player
        elif dealer.get_hand_value() > player.get_hand_value():
            dealer_win()
        # If the dealer's hand value is lower than 17
        elif dealer.get_hand_value() < 17:
            dealer.add_card_to_hand(deck.draw_card())
        # If the dealer's hand value is above 17 but below 21
        elif 17 <= dealer.get_hand_value() < 21:
            player_win()
        # If the dealer's got a blackjack
        elif dealer.get_hand_value() == 21:
            blackjack_dealer()


def check_funds():
    """
    Checks if the player has enough funds to play the round
    Exits the game if the player's chip count is below 2, which is the minimum amount to place a bet.

    :return: none
    """

    if player.get_funds() < 2:
        print("You cannot play with less than 2 chips in your bank. Better luck next time!")
        exit()
    else:
        return


def check_blackjack():
    """
    Checks if the player or the dealer has a "blackjack", meaning exact 21 card value in his hand

    :return: none
    """

    if player.get_hand_value() == 21 and dealer.get_hand_value() != 21:
        blackjack()
    if dealer.get_hand_value() == 21:
        blackjack_dealer()


def blackjack():
    """
    If this method is called, the player has a blackjack while the dealer does not and wins the round!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("Congratulation! You win the round!")
    print("You have a blackjack and the dealer hasn't!")

    # Pays the player 3 to 2
    winnings = round(player.get_bets() * 1.5)
    print("You bet a total of {} chips, you then win {} chips!".format(player.get_bets(), winnings))
    player.add_funds(player.get_bets())
    player.add_funds(winnings)
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    player.reset_bets()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def blackjack_dealer():
    """
    If this method is called, the dealer has a blackjack while the player does not.
    The player loses the round!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("The dealer has blackjack! You lose the round!")

    # The player loses all it's money
    print("You bet a total of {} chips, you lost everything!".format(player.get_bets()))
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    player.reset_bets()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def check_bust():
    """
    Checks if the player has gone "bust".

    :return: none
    """

    if player.get_hand_value() > 21:
        bust()


def bust():
    """
    If this method is called, the player has gone "bust" and loses the round!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("You've gone bust!")

    # Player loses all his bet money
    print("You bet a total of {} chips, you lost everything!".format(player.get_bets()))
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    # Money stuff
    player.reset_bets()

    # Checks if the player has enough funds to play another round
    check_funds()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def bust_dealer():
    """
    If this method is called, the dealer has bust and the player wins!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("The dealer has bust! You win the round!")

    # Pays the player the amount of his bet
    print("You bet a total of {} chips, you then win {} chips!".format(player.get_bets(), player.get_bets()))
    player.add_funds(player.get_bets() * 2)
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    player.reset_bets()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def player_win():
    """
    If this method is called, the player has a higher hand value than the dealer and wins the round!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("You have a higher hand value than the dealer! You win the round!")

    # Pays the player the amount of his bet
    print("You bet a total of {} chips, you then win {} chips!".format(player.get_bets(), player.get_bets()))
    player.add_funds(player.get_bets() * 2)
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    player.reset_bets()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

    # Shuffles the deck
    deck.shuffle_deck()

    # Starts a new round
    start_of_turn()


def dealer_win():
    """
    If this method is called, the dealer won!
    The player loses the round!

    :return: none
    """

    # Prints the board
    draw_board(True)

    print("You have a lower hand value than the dealer! You lose the round!")

    # The player loses all it's money
    print("You bet a total of {} chips, you lost everything!".format(player.get_bets()))
    print("You now have a total of {} chips.".format(player.get_funds()))
    print("")

    player.reset_bets()

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
        deck.add_card(card)
    player.reset_hand()
    for card in dealer.hand:
        deck.add_card(card)
    dealer.reset_hand()

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
