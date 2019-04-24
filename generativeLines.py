from turtle import *

#This program is WIP

def redWave(l):
    "Draws a red wave. Args: number of iterations of wave."
    pencolor("#ff0000")
    for waves in range(l):
        for turns in range(180):
            forward(0.1)
            right(1)
        for turns in range(180):
            forward(0.1)
            left(1)

    
