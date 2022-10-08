from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIR_UP = 90
DIR_RIGHT = 0
DIR_DOWN = 270
DIR_LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []

        for pos in START_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setpos(pos)
            self.segments.append(segment)

        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            self.segments[seg].setpos(self.segments[seg -1].xcor(), self.segments[seg -1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIR_DOWN:
            self.head.setheading(DIR_UP)
    
    def right(self):
        if self.head.heading() != DIR_LEFT:
            self.head.setheading(DIR_RIGHT)

    def down(self):
        if self.head.heading() != DIR_UP:
            self.head.setheading(DIR_DOWN)
    
    def left(self):
        if self.head.heading() != DIR_RIGHT:
            self.head.setheading(DIR_LEFT)
