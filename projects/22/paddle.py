from turtle import Turtle

SPEED = 0.3

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(6,1)
        self.setpos(x_pos, 0)
        self.y_vel = 0

    def move(self):
        self.setpos(self.xcor(), self.ycor() + self.y_vel)

    def up(self):
        self.y_vel = SPEED
    
    def down(self):
        self.y_vel = -SPEED

    def stop(self):
        self.y_vel = 0

