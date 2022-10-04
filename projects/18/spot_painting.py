# import colorgram
from turtle import Turtle, colormode
from random import choice
import turtle

timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.back(300)
timmy.right(90)
timmy.forward(300)
timmy.left(90)

timmy.shape("turtle")
colormode(255)


# colors = colorgram.extract('./projects/18/hirst_painting.jpg', 18)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
rgb_colors = [
    (181, 102, 22), (45, 104, 145), (128, 200, 187), (211, 161, 12),
    (14, 35, 60), (242, 83, 37), (210, 146, 117), (153, 185, 212),
    (238, 75, 91), (181, 46, 135), (97, 180, 47), (21, 91, 67),
    (253, 218, 0), (244, 217, 40)
]

def random_color():
    return choice(rgb_colors)

dot_size = 21
dot_gutter = 50
timmy.hideturtle()
timmy.up()
for x in range(100):
    if(x % 10 == 0 and x > 0):
        timmy.left(90)
        timmy.forward(dot_gutter)
        timmy.left(90)
        timmy.forward(10 * dot_gutter)
        timmy.left(180)

    timmy.dot(dot_size, random_color())
    timmy.forward(dot_gutter)

screen = turtle.Screen()
screen.exitonclick()
