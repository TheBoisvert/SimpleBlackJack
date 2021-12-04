from Classes import *
from random import shuffle


def starting_chip_count():
    multiple_repeats = False
    reply_list = ["Please, sir, this is a serious establishment.",
                  "Does this look like a joke to you?",
                  "Please, I'm not somebody who likes it's time wasted,",
                  "Very funny..."]

    while True:
        bank = input()

        if not bank.isnumeric() and not multiple_repeats:
            print("You can only play with money at this casino good sir. "
                  "So, how much will it be?")
            multiple_repeats = True
            continue
        elif not bank.isnumeric() and multiple_repeats:
            shuffle(reply_list)
            print(reply_list[0])
            continue
        elif bank.isnumeric() and int(bank) == 0:
            shuffle(reply_list)
            print(reply_list[0])
            multiple_repeats = True
            continue
        elif bank.isnumeric() and int(bank) < 25:
            print("We can't accept anything less than 25 chips here sir,"
                  "please present a bigger amount.")
            multiple_repeats = True
            continue
        elif bank.isnumeric() and int(bank) > 1000000000:
            print("Mmm, I'm not sure the house can match this price sir, "
                  "please play with a smaller amount...")
            multiple_repeats = True
            continue
        else:
            break

    return int(bank)


def start_of_turn():
    print("The minimum bets for this round is " + minimum_bet() + ".")
    print("Place your bet!")

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


def place_bet():
    multiple_repeats = False
    reply_list = ["Please, sir, this is a serious establishment.",
                  "Does this look like a joke to you?",
                  "Please, I'm not somebody who likes it's time wasted,",
                  "Very funny..."]

    while True:
        bet = input()

        if not bet.isnumeric() and not multiple_repeats:
            print("You can only play with money at this casino good sir. "
                  "So, how much will it be?")
            multiple_repeats = True
            continue
        elif not bet.isnumeric() and multiple_repeats:
            shuffle(reply_list)
            print(reply_list[0])
            continue
        elif bet.isnumeric() and int(bet) == 0:
            shuffle(reply_list)
            print(reply_list[0])
            multiple_repeats = True
            continue
        elif bet.isnumeric() and int(bet) > player.bank:
            print("You don't have enough chips! You need to bet a smaller amount...")
            multiple_repeats = True
            continue
        else:
            break

    return int(bet)


def minimum_bet():
    result = 5 * round((player.bank * 0.05) / 5)

    if result == 0:
        return "5"
    else:
        return str(result)


if __name__ == "__main__":

    print("Welcome gentleman, please take a seat...")
    print("How much money is on the table tonight?")

    player = Player(starting_chip_count())
    dealer = Dealer()

    print("Excellent, let's begin!" + "\n" + "\n")

    deck = Deck()
    deck.shuffle_deck()

    start_of_turn()
