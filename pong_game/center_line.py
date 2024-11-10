from turtle import Turtle

class Center_line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.add_line()
        self.move()
        
    def add_line(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        
    def move(self):
        y_axis = 320
        self.goto(0, y_axis)
        for line in range(y_axis, -y_axis, -40):
            self.pendown()
            self.goto(0, line)
            self.penup()
            self.goto(0, line - 20)

