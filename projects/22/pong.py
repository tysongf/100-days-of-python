from turtle import Screen

from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

SCREEN_W = 900
SCREEN_H = 600
BALL_SPEED = 1
PADDLE_SPEED = 1

screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)

playing = True
ball = Ball()
player_paddle = Paddle(SCREEN_W / 2 - 20)
cpu_paddle = Paddle(-SCREEN_W / 2 + 10)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_paddle.up, "Up")
screen.onkeyrelease(player_paddle.stop, "Up")
screen.onkeypress(player_paddle.down, "Down")
screen.onkeyrelease(player_paddle.stop, "Down")

screen.onkeypress(cpu_paddle.up, "a")
screen.onkeyrelease(cpu_paddle.stop, "a")
screen.onkeypress(cpu_paddle.down, "z")
screen.onkeyrelease(cpu_paddle.stop, "z")

screen.onkey(ball.start, "space")


while playing:
    player_paddle.move()
    cpu_paddle.move()
    ball.move()
    screen.update()

    # AI Paddle Movement

    # Detect wall collision
    if abs(ball.ycor()) > SCREEN_H / 2: ball.bounce_y()

    # Detect paddle collision
    if ball.x_vel > 0 and ball.distance(player_paddle) < 23: ball.bounce_x()
    if ball.x_vel < 0 and ball.distance(cpu_paddle) < 23: ball.bounce_x()

    # Detect goal collision
        # Increment score
        # Game Over when a player gets 10 points    


scoreboard.game_over()

screen.exitonclick()
