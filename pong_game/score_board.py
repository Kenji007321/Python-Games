from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Geogrotesque Sharp XCompressed Medium", 45, "bold"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Geogrotesque Sharp XCompressed Medium", 45, "bold"))
        
    def l_point(self):
        self.score_left += 1
        self.update_scoreboard()
        
    def r_point(self):
        self.score_right += 1
        self.update_scoreboard()