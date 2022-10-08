from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

WIDTH = 600
HEIGHT = 600
SNAKE_SPEED = 0.33
FOOD_SCORE = 10

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

playing = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while playing:
    time.sleep(SNAKE_SPEED)
    snake.move()
    screen.update()

    # Detect food collision
    if snake.head.distance(food) <= 15:
        print("Om nom nom")
        food.respawn()
        scoreboard.add_score(FOOD_SCORE)

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        playing = False

scoreboard.game_over()

screen.exitonclick()
