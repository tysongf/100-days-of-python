from turtle import Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

playing = True
snake = Snake()

while playing:
    snake.move()
    time.sleep(0.4)
    screen.update()

screen.exitonclick()
