from turtle import Turtle

class Snake:
    def __init__(self):
        start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for pos in start_positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.setpos(pos)
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) -1, 0, -1):
            self.segments[seg].setpos(self.segments[seg -1].xcor(), self.segments[seg -1].ycor())
        self.segments[0].forward(20)
