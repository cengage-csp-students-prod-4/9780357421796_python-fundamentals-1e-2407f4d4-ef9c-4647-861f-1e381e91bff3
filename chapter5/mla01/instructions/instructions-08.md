# Putting it All Together

Your task is to now combine everything together to create the blackjack game that is defined in the `create_blackjack_game(user_input)` function. In the first part of this task, you will implement the section marked with `# FIRST SECTION INSERT YOUR CODE HERE`. For this first section, you should do the following:

● Create a list for the player called ‘player’, which will hold the cards in the player’s hand, and then create another list for the dealer called ‘dealer’, which will hold the cards in the dealer’s hand.

● Create a new deck of cards using the `create_standard_deck()` function.

● Draw two cards for each player and add them to the respective player’s hands.

● Create two variables, one for each player, that stores the count of the player’s hands. The cards will be displayed using the `display_player(player)` function and the `display_dealer(opponent, start=true)` function. These functions have been written already, but will need to be placed correctly.

You then need to implement the second section marked with `# SECOND SECTION INSERT YOUR CODE HERE`. For this second section, you should do the following:

● Implement the logic for the player. The code has already been provided that prompts the user for an action and stores this in `player_action`. If the user action is **q**, then the game quits. You need to implement the part where the user provides an **h**, which stands for ‘hit’ (that is, for drawing a card), and **s**, which stands for ‘stay’ (that is, to stop drawing cards). After each card is drawn, the player’s hand needs to be checked to see whether they have won, they are bust, or whether everything is okay.You will need to implement `display_player(player)` and `display_dealer(opponent, start=true)` after each draw.

You then need to implement the third section marked with `# THIRD SECTION INSERT YOUR CODE HERE`. For this third section, you should do the following:

● Implement the logic for the dealer. The dealer will continue to ‘hit’ (that is, draw a new card) if the total count in their hand is lower than 17. During each ‘hit’, you must check whether the dealer has won, is bust, or is in the range from 17 to 20 (inclusive). If the dealer has a total value in the range from 17 to 20 (inclusive), then the dealer must stop drawing cards.

● After this, if no winner/loser has been decided (that is, each of the players has opted to stay at some point), a final comparison is made to see who has the highest total in their hands. The winner is the player with the highest total.

● At each point that represents an endpoint to the game (such as a bust, the count = 21, or the highest deck value if both players stay), you need to return an appropriate value. For example, if the player wins, return **1**, and if the dealer wins, then return **–1**.
