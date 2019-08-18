from turtle import *
from random import *

#This program is WIP

def pinkWave(l):
    "Draws a pink wave. Args: Number of iterations of wave."
    pencolor("#ff00cc")
    for waves in range(l):
        for turns in range(180):
            forward(0.1)
            right(1)
        for turns in range(180):
            forward(0.1)
            left(1)

def purpleStraightLine(l):
    "Draws a purple straight line. Args: Length of line."
    pencolor("#cc00ff")
    for pixels in range(l):
        forward(1)

def turquoiseDiamond(s):
    "Draws a turquoise diamond. Args: Size of diamond, s=length of one side."
    pencolor("#00ccff")
    forward(s)
    right(150)
    forward(s)
    right(30)
    forward(s)
    right(150)
    forward(s)

def blackZigZag(l):
    "Draws a black zigzag. Args: Number of iterations of zigzag."
    pencolor("#000000") #Color untested
    for zees in range(l):
        forward(12)
        right(143) #Approx sin^-1 (9/15)
        forward(15)
        left(143)
        forward(12)

hideturtle()
for lines in range(50):
    pinkWave(randint(1,6))
    purpleStraightLine(randint(1,200))
    right(randint(30,270))
    turquoiseDiamond(randint(1,50))
    blackZigZag(randint(1,10))
