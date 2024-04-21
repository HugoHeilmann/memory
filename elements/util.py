from turtle import *

def leftSquare(turtle):
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()

def rightSquare(turtle):
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

def rowLeftSquares(turtle, number):
    turtle.down()
    turtle.begin_fill()
    for i in range(number):
        leftSquare(turtle)
        turtle.forward(20)
    turtle.end_fill()

def rowRightSquares(turtle, number):
    turtle.down()
    turtle.begin_fill()
    for i in range(number):
        rightSquare(turtle)
        turtle.forward(20)
    turtle.end_fill()