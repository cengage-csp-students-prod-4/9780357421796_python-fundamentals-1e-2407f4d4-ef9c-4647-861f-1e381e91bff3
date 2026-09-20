from itertools import product
from random import choice, seed
from os import linesep


suits = {'hearts', 'clubs', 'spades', 'diamonds'}
numbers = set([i for i in range(2, 15)])
a = 551
seed(a)


# ---------------------------------------------------------------- Task #01
def create_standard_deck():
    """52 cards as (suit, number) tuples, sorted by suit then number."""
    return sorted(product(suits, numbers))


# ------------------------------------------------------------ query helpers
def get_all_cards(deck):
    return list(deck)


def get_all_twos(deck):
    return [card for card in deck if card[1] == 2]


def get_all_aces(deck):
    return [card for card in deck if card[1] == 14]


def get_card_number(deck, card_number):
    return [card for card in deck if card[1] == card_number]


def get_card_suit(deck, suit):
    return [card for card in deck if card[0] == suit]


def get_number_and_suit(deck, num, suit):
    return [card for card in deck if card[0] == suit and card[1] == num]


# ----------------------------------------------------------- remove helpers
def remove_card_from_deck(deck, suit, num):
    """Mutates deck in place. Removes one matching card; silent if absent."""
    card = (suit, num)
    if card in deck:
        deck.remove(card)
    return deck


def remove_suit_from_deck(deck, suit):
    for card in get_card_suit(deck, suit):
        deck.remove(card)
    return deck


def remove_number_from_deck(deck, number):
    for card in get_card_number(deck, number):
        deck.remove(card)
    return deck


# -------------------------------------------------------------- add helpers
def add_card_to_deck(deck, suit, num):
    deck.append((suit, num))
    deck.sort()
    return deck


def add_suit_to_deck(deck, suit):
    for num in sorted(numbers):
        deck.append((suit, num))
    deck.sort()
    return deck


def add_number_to_deck(deck, number):
    for suit in sorted(suits):
        deck.append((suit, number))
    deck.sort()
    return deck


# ---------------------------------------------------------------- Task #02
def draw_card(deck):
    """Pick a random card, remove it from the deck, return it."""
    card = choice(deck)
    remove_card_from_deck(deck, card[0], card[1])
    return card


# ---------------------------------------------------------- display (given)
def display_dealer(opponent, start=False):
    print('Dealer:')
    if start:
        the_output = [opponent[0], ('?', '?')]
        print(the_output)
    else:
        print(opponent)


def display_player(player):
    print('Player:')
    print(player)


# ---------------------------------------------------------------- Task #03
def get_count(player):
    """J/Q/K (11,12,13) -> 10, Ace (14) -> 11, everything else face value."""
    total = 0
    for suit, number in player:
        if number in (11, 12, 13):
            total += 10
        elif number == 14:
            total += 11
        else:
            total += number
    return total


# ---------------------------------------------------------------- Task #04
def check_cards(player):
    count = get_count(player)
    if count == 21:
        return 'WIN'
    elif count > 21:
        return 'BUST'
    return 'OK'


# ---------------------------------------------------------------- Task #05
def create_blackjack_game(user_input):
    # FIRST SECTION INSERT YOUR CODE HERE
    player = []
    dealer = []

    deck = create_standard_deck()

    for _ in range(2):
        player.append(draw_card(deck))
        dealer.append(draw_card(deck))

    player_count = get_count(player)
    dealer_count = get_count(dealer)

    display_player(player)
    display_dealer(dealer, start=True)

    if not user_input:
        player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
        while player_action not in ('s', 'h', 'q'):
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
    else:
        player_action = user_input.pop(0)

    if player_action == 'q':
        return 0
    while player_action != 'q':

        if player_action == 'h':
            # SECOND SECTION INSERT YOUR CODE HERE
            player.append(draw_card(deck))
            player_count = get_count(player)

            display_player(player)
            display_dealer(dealer, start=True)

            status = check_cards(player)
            if status == 'WIN':
                return 1
            elif status == 'BUST':
                return -1
        else:
            while True:
                # THIRD SECTION INSERT YOUR CODE HERE
                dealer_count = get_count(dealer)

                display_player(player)
                display_dealer(dealer)

                status = check_cards(dealer)
                if status == 'WIN':
                    return -1
                elif status == 'BUST':
                    return 1

                if dealer_count < 17:
                    dealer.append(draw_card(deck))
                    continue

                player_count = get_count(player)
                if player_count > dealer_count:
                    return 1
                return -1

        if not user_input:
            player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            while player_action not in ('s', 'h', 'q'):
                player_action = input('press h to hit, s to stand, q to quit.').lower().strip(linesep)
            if player_action == 'q':
                return 0
        else:
            player_action = user_input.pop(0)

    return 0