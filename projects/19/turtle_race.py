from turtle import Turtle, Screen
from racer import Racer
import random

screen = Screen()
screen.setup(width=600, height=400)
turtle_speed = 3

leo = Racer(Turtle(), "blue", "blue", "turtle", -280, 160)
don = Racer(Turtle(), "purple", "blue violet", "turtle",  -280, 70)
mike = Racer(Turtle(), "yellow", "orange", "turtle",  -280, 0)
raph = Racer(Turtle(), "red", "red", "turtle",  -280, -70)
april = Racer(Turtle(), "green", "green", "turtle",  -280, -160)

turtles = [leo, don, mike, raph, april]

bet = screen.textinput("Make your bet", "Which turtle will win the race? (blue, purple, yellow, red, green): ")

finished_turtles = {}
racing = True
finish_position = 0
winner = ""
while racing:
    mover = random.choice(turtles)
    mover.turtle.forward(turtle_speed)
    if(mover.turtle.xcor() > screen.window_width() / 2):
        if not mover.finished:
            finish_position += 1
            if finish_position == 1:
                winner = mover.name
            finished_turtles[mover.name] = finish_position
            mover.finished = True
            if(len(finished_turtles) == len(turtles)):
                racing = False


if(finished_turtles[bet] == 1):
    print(f"Your {bet} turtle is the winner!")
else:
    print(f"{winner.title()} is the winner!")
    print(f"Your {bet} turtle finished at position {finished_turtles[bet]}")

screen.exitonclick()
