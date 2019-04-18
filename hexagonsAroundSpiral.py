from turtle import *
hideturtle()
i = 0.5
for x in range(36):
    pen(pencolor="#883300", pensize=2)
    for y in range(60):
        right(1)
        forward(i)
    pen(pencolor="#cc00ff", pensize=2)
    for z in range(6):
        right(60)
        forward(25)
    i = i + 0.1
