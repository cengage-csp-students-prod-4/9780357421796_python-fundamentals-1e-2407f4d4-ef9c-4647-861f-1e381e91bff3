## Make it your own

Extend the implementation of blackjack to work with multiple decks. This involves creating several decks and then executing the same logic, as mentioned previously, for the blackjack game. Note that with multiple decks, it’s possible to get multiple copies of the same card. For example, a player may get a hand consisting of (‘clubs’, 2), (‘clubs’, 2), and so on.

Further extend the implementation of blackjack with cheat decks (or missing cards); that is, create decks with known missing cards and ensure that the blackjack logic still works. For example, it should be possible to create decks consisting entirely of Aces and picture cards. This would drastically increase the number of times either player has a hand consisting of a value of 21.

Create a “card counting” scheme to keep track of the running count. First, you will need to extend the game logic to create a discard pile. The discard pile contains all the cards that have been used in the previous hands and starts off empty. Create a system that tracks the cards the player has observed and use this information to display the probability of a player drawing a picture card. For this, you should assume that the deck is a complete standard deck. This probability should be printed to the screen and should be “live” in that it updates each time a card is revealed to the player.
