# SimpleBlackJack
#### A simple 1 player against computer dealer blackjack game that plays in the Terminal!

I tried to follow the rules of blackjack as much as possible.
I've taken the rules from this website : https://bicyclecards.com/how-to-play/blackjack/

Please feel free to report any bugs!

#### Notes and tweaks
This plays with a single pack of cards.  
The cards are placed back into the deck and the deck shuffled after each round, no card counting allowed ;)  
Betting limits follow general rule, minimum of 2 and maximum of 500.  
The dealer's bank is infinite.

I figured that letting players split pairs would add a lot of 
complexity  to the code, while not really adding much in terms of value
to the game. Since this is only supposed to be a simple python exercise, I decided 
not to include this mechanic to the game!  
The same is true for doubling down and for insurance.