from turtle import Turtle
import random

MIN_POS = -260
MAX_POS = 260

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        self.goto(random.randint(MIN_POS, MAX_POS), random.randint(MIN_POS, MAX_POS))
