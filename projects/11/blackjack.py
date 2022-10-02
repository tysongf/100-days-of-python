import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♠️", "♣️", "♥️", "♦️"]
dealer_cards = []
player_cards = []
credits = 100.00
bet = 0.00
drawing = True
playing = True


def table_ui():
    clear()
    print(f"Dealer: {display_cards(dealer_cards)} = {get_hand_value(dealer_cards)}\n")
    print(f"Player: {display_cards(player_cards)} = {get_hand_value(player_cards)}\n")


def display_cards(hand):
    output = ""
    for card in hand:
        output += f"{card['suit']}{card['face']} "
    return output


def get_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        value += get_card_value(card)
        if card['face'] == "A": aces += 1
    while (value > 21 and aces > 0):
        value -= 10
        aces -= 1
    return value


def get_card_value(card):
    if card['face'] == "A":
        return 11
    elif card['face'] == "K":
        return 10
    elif card['face'] == "Q":
        return 10
    elif card['face'] == "J":
        return 10
    else:
        return int(card['face'])


def new_card():
    return {"face": random.choice(cards), "suit": random.choice(suits)}


def hit(hand):
    hand.append(new_card())


def new_game():
    global player_cards, dealer_cards
    player_cards = [new_card(), new_card()]
    dealer_cards = [new_card()]
    game_loop()


def last_card(hand):
    return f"{hand[len(hand) - 1]['suit']}{hand[len(hand) - 1]['face']}"


def dealer_turn():
    global dealer_cards, player_cards, bet
    while get_hand_value(dealer_cards) < 17:
        hit(dealer_cards)
        table_ui()
        input(f"Dealer draws {last_card(dealer_cards)}")
    if (get_hand_value(dealer_cards) > 21):
        print("Dealer Busts!")
        input(f"You won {bet} credits!")
        win()
    elif len(dealer_cards) == 2 and get_hand_value(dealer_cards) == 21:
        print("Dealer has BlackPython!")
        input("You Lost! ")
        take_bet()
    elif get_hand_value(dealer_cards) <= 21:
        print("Dealer Stands!")
    if get_hand_value(dealer_cards) < get_hand_value(player_cards):
        input(f"You Won {bet} credits! ")
        win()
    elif (get_hand_value(dealer_cards) > get_hand_value(player_cards)):
        input("You Lost!\n")
        take_bet()
    else:
        print("Push!")
        input(f"You receive {bet} credits. ")
        push()


def push():
    global credits, bet
    credits += bet
    take_bet()


def win():
    global credits, bet
    credits += bet * 2
    take_bet()


def bj():
    global credits, bet
    winnings = bet * 2.5
    print("BlackPython!")
    input(f"You won {winnings}")
    credits += winnings
    take_bet()


def take_bet():
    global playing, credits, bet
    bet = 0
    while bet <= 0:
        clear()
        print(f"Credits: {credits}\n")
        bet = float(input("Place your Bet: "))
        if bet > credits:
            bet = 0
            input("Not enough credits! ")
        elif bet < 0:
            input("Invalid bet! ")
    credits -= bet
    new_game()


def game_loop():
    global drawing, player_cards
    drawing = True
    while drawing:
        clear()
        table_ui()
        if get_hand_value(player_cards) == 21:
            bj()
            return
        if get_hand_value(player_cards) > 21:
            input("Bust!")
            take_bet()
        action = input("(h)it or (s)tand : ")
        if action == "h":
            hit(player_cards)
            print(f"You draw a {last_card(player_cards)}\n")
        elif action == "s":
            drawing = False
            dealer_turn()


clear()
print("Welcome to BlackPython!\n")
input("Tip: Bet some letters to crash and exit the game. ")

take_bet()
