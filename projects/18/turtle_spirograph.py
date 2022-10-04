from turtle import Turtle, colormode
from random import randint, choice
import turtle

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy = Turtle()
timmy.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(choice(colors))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()
