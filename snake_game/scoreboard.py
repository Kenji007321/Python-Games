from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./snake_game/data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    def clear_score(self):
        self.clear()
        
    def update_scoreboard(self):
        self.clear_score()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over.", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./snake_game/data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()