from Classes import *
from random import shuffle


def starting_chip_count():
    while True:
        print("How many chips would you like to play with?")
        bank = input()

        if not bank.isnumeric():
            print("This is not a valid chip count.")
            continue
        elif bank.isnumeric() and int(bank) == 0:
            print("You cannot play with 0 chips.")
            continue
        elif bank.isnumeric() and int(bank) < 25:
            print("You cannot play with less than 25 chips.")
            continue
        elif bank.isnumeric() and int(bank) > 1000000000:
            print("You cannot play with more than 1,000,000 chips.")
            continue
        else:
            print("")
            break

    return int(bank)


def start_of_turn():
    print("The minimum bet for this round is " + minimum_bet() + ".")

    check_funds()

    place_bet()

    player.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())
    player.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())

    print("\n" + "The Dealer's hand :")
    for card in dealer.hand:
        if card == dealer.hand[-1]:
            print("~~~")
        else:
            print(card)

    print("\n" + "Your hand :")
    for card in player.hand:
        print(card)


def minimum_bet():
    result = round(player.bank * 0.05)

    if result < 5:
        return "5"
    else:
        return str(result)


def check_funds():
    if player.get_funds() < 25:
        print("You cannot play with less than 25 chips in your bank!")
        print("Better luck next time!")
        exit()
    else:
        return


def place_bet():
    while True:
        print("Place your bet!")
        bet = input()

        if not bet.isnumeric():
            print("This is not a valid chip count.")
            continue
        elif int(bet) > player.get_funds():
            print("You cannot bet more chips than what you have in your bank!")
            continue
        else:
            break

    table.add_to_bets(int(bet))


if __name__ == "__main__":

    player = Player(starting_chip_count())
    dealer = Dealer()
    table = Table()

    deck = Deck()
    deck.shuffle_deck()

    start_of_turn()
