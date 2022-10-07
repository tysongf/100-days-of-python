from turtle import Screen
from snake import Snake
import random
import time

SNAKE_SPEED = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

playing = True
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while playing:
    snake.move()
    time.sleep(SNAKE_SPEED)
    screen.update()

screen.exitonclick()
