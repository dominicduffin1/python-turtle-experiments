from turtle import *
hideturtle()
for x in range(6):
    pen(pencolor="#3300aa", pensize=4)
    right(60)
    forward(45)
    pen(pencolor="#bb00ee", pensize=4)
    for y in range(360):
        right(1)
        forward(1)
