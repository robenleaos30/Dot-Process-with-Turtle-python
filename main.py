import random
import turtle as t
from turtle import Screen

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'black']
t.colormode(255)
t.penup()
t.speed('fastest')
t.setheading(225)
t.hideturtle()
t.forward(250)
t.setheading(0)
num_dot = 100
for dot in range(1, num_dot + 1):
    t.dot(20, random.choice(colors))
    t.forward(50)

    if dot % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = Screen()
screen.exitonclick()
