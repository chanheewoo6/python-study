import turtle
import random

wn = turtle.Screen()
wn.title("Super Mario Mini")
wn.bgcolor("lightblue")
wn.setup(width= 800, height=600)
wn.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.color("red")
player.penup()
player.goto(0, -250)
player.distance = "Stop"



def move_left():
    x = player.xcor
    x -= 3
    player.setx(x)

def move_right():
    x = player.xcor
    x += 3
    player.setx(x)

wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")