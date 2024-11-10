from turtle import Screen
from paddle import Paddle
from score_board import Score
from center_line import Center_line
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_player = Paddle(350)
l_player = Paddle(-350)
score = Score()
center_line = Center_line()
ball = Ball()

screen.listen()
screen.onkey(r_player.go_up, "Up")
screen.onkey(r_player.go_down, "Down")

screen.onkey(l_player.go_up, "w")
screen.onkey(l_player.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    
    # Detect collision with screen.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move_speed *= 0.9
        
    # Detect collision with paddle.
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9
        
    # Detect if the ball has passed the screen, and speed up.
    if ball.xcor() > 390:
        score.l_point()
        ball.refresh()
        
    if ball.xcor() < -390:
        score.r_point()
        ball.refresh()
        




screen.exitonclick()