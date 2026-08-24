# Scenario

You’ve just been hired by a small-town casino that wants to create a simulated card playing platform. To get you warmed up, they want you to be able to create a blackjack game simulator.

The game logic needs to follow this pattern:

1. Create a deck.
2. Give each player two cards (chosen randomly using random.choice).
3. Display both hands
4. Prompt the player to either hit (that is, draw another card) or stay.
5. If the player hits, keep checking whether the total value of the player’s cards is equal to 21. If it is, then the player wins, and if it is above 21, then the player loses. Display each updated hand after each card draw.
6. If the player stays, then it’s the dealer’s turn to act. If the total value in the dealer’s hand is less than 17, then they must hit. If it is greater than or equal to 17 but less than or equal to 21, then the dealer must stay. If at any time the dealer’s total value is above 21, then the dealer busts and the player wins.
7. Finally, if both the player and dealer scores are below 21, and no one has busted yet, the player with the highest total wins. In the case of a tie, the dealer wins.

# Best Practices to Follow:

It’s worth breaking up each functional task in create_blackjack_game() into separate functions. For example, a function to check the score of a player’s hand, to check whether a player has won, and so on. This entire implementation can be done neatly in about eight functions.

# Create a Deck of Cards

Complete the `create_standard_deck()` function, which creates a new deck. The deck itself must be a data structure list. The cards within the deck must be represented as tuples of the form (suit, number), where the suit is a string that must be either ‘hearts’, ‘clubs’, ‘spades’, or ‘diamonds’, and the number is an integer that must be one of the following: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, or 14. Note that the number used to identify the card has the following association: Jack = 11, Queen = 12, King = 13, and Ace = 14. In terms of value, the picture cards (Jack, Queen, and King) all have a value of 10, and the Ace card has a value of 11. The casino only wants you to implement a simple implementation of blackjack, in that the first to 21 wins, and special cases for checking for blackjack are not required. The deck should be sorted in alphabetical order of the suit, and then by an ascending integer identifier; for example: [(‘clubs’, 2), (‘clubs’, 3), ..., (‘diamonds’, 2), ..., (‘diamonds’, 14), (‘hearts’, 2), ... , (‘spades’, 14)].
