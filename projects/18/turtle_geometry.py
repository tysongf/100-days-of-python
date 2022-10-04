from turtle import Turtle, colormode
from random import randint, choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy = Turtle()
timmy.speed(7)

timmy.shape("turtle")
timmy.color("MediumPurple", "DeepPink")
timmy.penup()
timmy.setpos(-100, -200)
timmy.pendown()

for shape_sides in range(3, 9):
    timmy.color(choice(colors))
    angle = 360 / shape_sides
    for _ in range(0, shape_sides):
        timmy.forward(200)
        timmy.left(angle)

input()
