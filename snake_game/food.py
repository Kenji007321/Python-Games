from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["blue", "green", "red", "orange", "purple", "navy", "yellow", "pink"]
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(self.colors))
        self.speed("fastest")
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
    
    def new_color(self):
        self.color(random.choice(self.colors))
        
    def refresh(self):
        self.new_color()
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)