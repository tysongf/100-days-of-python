from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_fwd():
    timmy.forward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def toggle_pen():
    if(timmy.isdown()):
        timmy.penup()
    else:
        timmy.pendown()

screen.listen()
screen.onkey(key="space", fun=toggle_pen)
screen.onkey(key="Up", fun=move_fwd)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.exitonclick()
