from turtle import Turtle

WIDTH = 3
LENGTH = 0.5
PADDLE_COLOR = "white"

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.add_paddle(position)
         
    def add_paddle(self, position):
        self.shape("square")
        self.penup()
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.setposition(position, 0)
        
    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)