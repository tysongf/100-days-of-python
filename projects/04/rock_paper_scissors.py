import random

elements = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Rock, Paper, or Scissors?\n  0: Rock\n  1: Paper\n  2: Scissors\n> "))

valid_choice = user_choice >= 0 and user_choice < 3

#   | R | P | S |
# R | T | L | W |
# P | W | T | L |
# S | L | W | T |

if valid_choice:
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {elements[computer_choice]}")

    outcomes = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
    result = outcomes[user_choice][computer_choice]

    if result == -1:
        print("You Lose!")
    elif result == 0:
        print("It's a Draw!")
    else:
        print("You Won!")
else:
    print("Invalid Number. You Lose!")
