class Racer:
    def __init__(self, turtle, name, color, shape, x, y):
        turtle.penup()
        self.turtle = turtle
        self.name = name
        self.turtle.shape(shape)
        self.turtle.color(color)
        self.turtle.goto(x=x, y=y)
        self.finished = False
