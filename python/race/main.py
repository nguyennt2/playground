from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.bgcolor('black')
screen.setup(width=500, height=400)

colors = ["red", "green", "blue", "orange", "pink"]
turtles = []
for index in range(0, len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.speed(3)
    new_turtle.goto(x=-230, y=(100 - index*50))
    turtles.append(new_turtle)

is_still_alive = True
while is_still_alive:
    for index in range(0, len(turtles)):
        turtles[index].forward(randint(0, 20))
        if int(turtles[index].xcor()) >= 210:
            is_still_alive = False
            print(f"The winner is {colors[index]} turtle.")


screen.exitonclick()
