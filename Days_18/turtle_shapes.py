from turtle import Turtle, Screen
import heroes

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

shapes = [
    {"name": "triangle", "sides": 3,  "color": "red"},
    {"name": "square",   "sides": 4,  "color": "blue"},
    {"name": "pentagon", "sides": 5,  "color": "gold"},
    {"name": "hexagon",  "sides": 6,  "color": "green"},
    {"name": "heptagon", "sides": 7,  "color": "red"},
    {"name": "octagon",  "sides": 8,  "color": "blue"},
    {"name": "nonagon",  "sides": 9,  "color": "gold"},
    {"name": "decagon",  "sides": 10, "color": "green"}
]

y_position = 0
for shape in shapes:
    y_position += 20
    print(f"Now drawing: {shape["name"]}")
    timmy.color(shape["color"])
    timmy.forward(100)
    shape_sides = shape["sides"]
    angle = 360/shape_sides
    for i in range(shape_sides):
        timmy.right(angle)
        timmy.forward(100)

    timmy.penup()
    timmy.setpos(0.00,y_position)
    timmy.pendown()

screen = Screen()
screen.exitonclick()