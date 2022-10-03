import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


difficulty_guesses = {
    "e": 9,  # easy
    "n": 7,  # normal
    "d": 5,  # difficult
}


def new_game():
    clear()
    secret_number = random.randint(1, 101)
    d = 0
    while (d not in ["e", "n", "d"]):
        d = input("\nSelect Difficulty\n\n(e)asy (n)ormal (d)ifficult: ")
    clear()

    num_guesses = difficulty_guesses[d]
    guess = 0

    while (num_guesses > 0 and guess != secret_number):
        print(f"\n{num_guesses} guesses left.\n")
        guess = int(input("Guess: "))
        num_guesses -= 1
        if (guess > secret_number):
            print("\nToo High")
        elif (guess < secret_number):
            print("\nToo Low")

    if (guess == secret_number):
        print("\n🎉🎉🎉 You Got It 🎉🎉🎉\n")
    else:
        print("\n💩💩💩 You Lose 💩💩💩\n")

    play_again = ""
    while (play_again not in ["y", "n"]):
        play_again = input("Play Again? y / n: ")

    if (play_again == "y"):
        new_game()


new_game()
