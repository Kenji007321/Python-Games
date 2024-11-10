import random
from turtle import Turtle

# RANDOM_Y = (10, -10)
# RANDOM_X = (10, -10)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.random_y = [10, -10]
        self.random_x = [10, -10]
        self.create_ball()
        self.x_move = random.choice(self.random_x)
        self.y_move = random.choice(self.random_y)
        self.move_speed = 0.1
        
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.setposition(x=0, y=0)
        
    def move_ball(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.speed(5)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def refresh(self):
        self.setposition(x=0, y=0)
        self.move_speed = 0.1
        self.bounce_x()
        