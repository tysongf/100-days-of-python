from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

playing = True

start_positions = [(0, 0), (-20, 0), (-40, 0)]
snake = []
snake_size = 3
def create_snake():
    for pos in start_positions:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.setpos(pos)
        snake.append(segment)

create_snake()

screen.update()

while playing:
    for seg in range(len(snake) -1, 0, -1):
        snake[seg].setpos(snake[seg -1].xcor(), snake[seg -1].ycor())
    snake[0].forward(20)
    time.sleep(0.4)
    screen.update()


screen.exitonclick()
