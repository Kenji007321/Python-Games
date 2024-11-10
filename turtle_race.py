from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["blue", "green", "yellow", "orange", "red"]
all_turtles = []


def linup(name, color_var, position_y):
    name = Turtle(shape="turtle")
    name.color(color_var)
    name.penup()
    name.goto(x=-230, y=position_y)
    all_turtles.append(name)

linup("blue", colors[0], -100)
linup("green", colors[1], -50)
linup("yellow", colors[2], 0)
linup("orange", colors[3], 50)
linup("red", colors[4], 100)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True
    
while is_race_on == True:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost.. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    


screen.exitonclick()

