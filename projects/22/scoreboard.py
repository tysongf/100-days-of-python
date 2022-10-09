from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.cpu_score = 0
        self.player_score = 0
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 260)
        self.write(f"{self.cpu_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 260)
        self.write(f"{self.player_score}", align=ALIGNMENT, font=FONT)

    def player_scored(self, points):
        self.player_score += points
        self.draw_score()

    def Cpu_scored(self, points):
        self.cpu_score += points
        self.draw_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

