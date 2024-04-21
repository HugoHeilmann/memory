import turtle
import time
import util

def piece(t, color):
    t.speed(100)

    # Contour noir
    util.row_right_squares(t, 4)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 8)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 4)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 8)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 2)

    # Encrage
    t.color(color)
    t.begin_fill()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(160)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(160)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.end_fill()

    # Coeur
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.color("#000000")
    util.row_right_squares(t, 2)
    t.left(90)
    util.row_right_squares(t, 8)
    t.left(90)
    util.row_right_squares(t, 2)
    t.left(90)
    util.row_right_squares(t, 8)

    time.sleep(5)

t = turtle.Turtle()
piece(t, "#880000")
    