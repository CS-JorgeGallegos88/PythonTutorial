from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.width(20)
timmy.speed(0)

angles = [0, 90, 180, 270]
colors = ["DodgerBlue", "gold", "firebrick", "HotPink", "LightSeaGreen", "purple"]

def random_walk(num):
    for i in range(num):
        timmy.color(random.choice(colors))
        timmy.forward(50)
        timmy.setheading(random.choice(angles))

random_walk(500)
screen = Screen()
screen.exitonclick()