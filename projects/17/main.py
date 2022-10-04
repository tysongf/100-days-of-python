from player import Player
from quiz_brain import QuizBrain
from question_model import question_bank


quiz_brain = QuizBrain(question_bank)

def start_game():

    player_name = input("\nEnter your name: ")
    player = Player(player_name)

    playing = True
    while playing:

        player_answer = ""
        print(f"\n{quiz_brain.get_question().text}\n")
        while player_answer not in ["t", "f"]:
            player_answer = input("(t)rue or (f)alse? ")
        
        if player_answer == "t":
            if quiz_brain.get_question().answer == "True":
                player.add_right()
            else:
                player.add_wrong()
        else:
            if quiz_brain.get_question().answer == "False":
                player.add_right()
            else:
                player.add_wrong()
        
        if not quiz_brain.next_question():
            print(f"Nice work, {player.name}!\n")
            print(f"You got {player.right} answers correct and {player.wrong} incorrect.\n")

            player.reset_score()

            play_again = input("Want to play again? y/n: ")
            if play_again != "y":
                playing = False
                print("\nGoodbye!\n")

start_game()
