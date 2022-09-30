import random

word_list = ["aardvark", "baboon", "camel", "hamster", "urangutan", "cheetah", "porcupine", "quail", "dolphin"]

secret_word = random.choice(word_list)
letters_guessed = []
health = ["❤️", "❤️", "❤️", "❤️", "❤️"]
game_over = 0

def print_ui():
    print(f"\nHealth: {health}\n")
    print(solution)

solution = []
for char in secret_word:
    solution.append("_")

total_matches = 0

while(game_over == 0):
    
    print_ui()
    guess = input("\nPick a letter: ")
    
    if guess not in letters_guessed:
        matches = 0
        letters_guessed.append(guess)
        
        for n in range(0, len(secret_word)):
            if(secret_word[n] == guess):
                solution[n] = guess
                matches += 1
                total_matches += 1
        
        if total_matches == len(solution):
            game_over = 1

        if matches == 0:
            health.pop()
            if len(health) == 0:
                game_over = -1
            else:
                print(f"\nFound {matches} '{guess}'\n")
    else:
        print("You already guessed that letter!")

if(game_over == 1):
    print_ui()
    print("\n🌈 You Won!\n")
if(game_over == -1): print("\n💀 You Lost!\n")
