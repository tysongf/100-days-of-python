from turtle import Turtle, colormode
from random import randint, choice

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy = Turtle()
timmy.speed(5)
timmy.pensize(10)

timmy.shape("turtle")
colormode(255)

turns = [0, 90, 180, 270]
# turns = [0, 45, 90, 135, 180, 225, 270, 315]
distance = [20, 40, 60]

for _ in range(0, 100):
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    turn = choice(turns)
    # dist = choice(distance)
    dist = 50
    timmy.setheading(turn)
    timmy.forward(dist)    

