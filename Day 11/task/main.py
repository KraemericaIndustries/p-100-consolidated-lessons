import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card(hand):
    hand.append(cards[random.randint(0, len(cards) - 1)])
    #hand.append(cards[0])
def add_cards(hand):
    score = 0
    for card in hand:
        score += card
    return score

def show_score():
    print(f"   Your cards:{player_hand}, current score: {player_score}")
    print(f"   Computer's first card: {computer_hand[0]}")

def show_final_hand():
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

def determine_winner():
    if player_score > 21:
        print("Player busts.  Dealer wins! :-(")
    elif computer_score > 21:
        print("Dealer busts.  Player wins! :-)")
    elif player_score > computer_score:
        print("Player wins! :-)")
    elif computer_score > player_score:
        print("Computer wins! :-(")
    else:
        print("It's a draw.  :-|")

def bust():
    show_final_hand()
    print("bust(): You went over.  You lose :-(")

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y":
    print("\n" * 100)
    player_hand = []
    computer_hand = []
    player_score = 0
    computer_score = 0
    print(art.logo)

    # Deal Players initial hand... (These 2 for loops *could* be consolidated).
    for number in range(0, 2):
        get_card(player_hand)

    # Deal Computers initial hand...
    for number in range(0, 2):
        get_card(computer_hand)

    player_score = add_cards(player_hand)
    show_score()
    want_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while want_card == "y":
        get_card(player_hand)
        player_score = add_cards(player_hand)
        if player_score > 21:
            if 11 in player_hand:
                print("Changing Ace from 11 points to 1...") # These two blocks could be extracted to a function
                x = player_hand.index(11)
                player_hand[x] = 1
                player_score += -10
                print(f"   Your cards:{player_hand}, current score: {player_score}")
                want_card = input("Type 'y' to get another card, type 'n' to pass: ")
            else: break
        else:
            show_score()
            want_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # Want another card = No
    while computer_score < player_score and player_score <= 21:
        get_card(computer_hand)
        computer_score = add_cards(computer_hand)
        if computer_score == 21:
            break
        elif computer_score > 21:
            if 11 in computer_hand:
                x = computer_hand.index(11)
                computer_hand[x] = 1
                computer_score += -10
            # break
    computer_score = add_cards(computer_hand)
    show_final_hand()
    determine_winner()
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print("***Fine.  Be that way.  Go Fuck yourself.***")
