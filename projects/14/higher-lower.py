import game_data
import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()


def game_loop():
    global game_data
    questions = random.sample(game_data.data, len(game_data.data))
    high_score = 0
    score = 0
    playing = True
    current_index = 0
    next_index = 1

    while playing:
        clear()
        current_item = questions[current_index]
        next_item = questions[next_index]

        print(f"{current_item['name']}")
        print(f"{current_item['description']}")
        print(f"{current_item['country']}")
        print(f"\n{current_item['follower_count']} Million Followers")

        print("\n--------------- VS ---------------\n")
        current_item = questions[current_index]
        next_item = questions[next_index]

        print(f"name: {next_item['name']}")
        print(f"description: {next_item['description']}")
        print(f"country: {next_item['country']}")

        guess = ""
        while guess != "h" and guess != "l":
            guess = input(
                f"\n\nIs {next_item['name']}'s follower count (h)igher or (l)ower than {current_item['name']}'s {current_item['follower_count']} Million followers? ")

        if guess == "h":
            if next_item['follower_count'] >= current_item['follower_count']:
                print("\nCorrect!")
                score += 1
            else:
                print("\nWrong!")
                playing = False

        if guess == "l":
            if next_item['follower_count'] <= current_item['follower_count']:
                print("\nCorrect!")
                score += 1
            else:
                print("\nWrong!")
                playing = False

        input(f"\n{next_item['name']} has {next_item['follower_count']} Million Followers ")

        current_index += 1
        next_index += 1

    print(f"\nFinal Score: {score} 🎉\n")


game_loop()
