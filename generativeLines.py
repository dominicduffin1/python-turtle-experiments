from turtle import *

#This program is WIP

def redWave(l):
    "Draws a red wave. Args: Number of iterations of wave."
    pencolor("#ff0000")
    for waves in range(l):
        for turns in range(180):
            forward(0.1)
            right(1)
        for turns in range(180):
            forward(0.1)
            left(1)

def blueStraightLine(l):
    "Draws a blue straight line. Args: Length of line."
    pencolor("#0000ff")
    for pixels in range(l):
        forward(1)

def greenDiamond(s):
    "Draws a green diamond. Args: Size of diamond, s=length of one side."
    pencolor("#00ff00")
    forward(s)
    right(150)
    forward(s)
    right(30)
    forward(s)
    right(150)
    forward(s)

def yellowZigZag(l):
    "Draws a yellow zigzag. Args: Number of iterations of zigzag."
    pencolor("#ffff00") #Color untested
    for zees in range(l):
        forward(12)
        right(143) #Approx sin^-1 (9/15)
        forward(15)
        left(143)
        forward(12)

    
