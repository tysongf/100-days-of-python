from turtle import Turtle
import random

START_POSITION = (0, 0)
SPEED = 0.2

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")        
        self.reset()
        self.y_vel = 0
        self.x_vel = 0

    def reset(self):
        self.setpos(START_POSITION)

    def start(self):
        self.x_vel = 0.3
        self.y_vel = random.choice([SPEED, -SPEED])

    def move(self):
        self.setpos(self.xcor() + self.x_vel, self.ycor() + self.y_vel)

    def bounce_y(self):
        self.y_vel *= -1

    def bounce_x(self):
        self.x_vel *= -1
