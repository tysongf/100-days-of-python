from turtle import Screen
from snake import Snake
from food import Food
import time

SNAKE_SPEED = 0.33

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

playing = True
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while playing:
    time.sleep(SNAKE_SPEED)
    snake.move()
    screen.update()

screen.exitonclick()
