from turtle import Turtle, colormode
from random import randint
import time

timmy = Turtle()
timmy.speed(10)
colormode(255)

timmy.shape("turtle")
timmy.color("MediumPurple", "DeepPink")
timmy.penup()
timmy.setpos(-100, -200)
timmy.pendown()

for shape_sides in range(3, 9):
    timmy.color(randint(0,255), randint(0,255), randint(0,255))
    angle = 360 / shape_sides
    for _ in range(0, shape_sides):
        timmy.forward(200)
        timmy.left(angle)

time.sleep(10)
