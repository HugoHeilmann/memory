import usefull
import turtle
import time

def buisson(t, pixel_size) :
    t.speed(100)

    # Contour noir
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 5, pixel_size)
    t.backward(5*pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    usefull.row_left_squares(t, 1, 2*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 1, 2*pixel_size)
    t.left(180)
    t.forward(3*pixel_size)

    # Remplissage vert
    t.color("#00FF00")
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(2*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.forward(3*pixel_size)
        t.left(90)
        t.forward(5*pixel_size)
        t.left(90)
    t.end_fill()
    t.left(90)
    t.forward(3*pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 5, pixel_size)

    time.sleep(5)

t = turtle.Turtle()
buisson(t, 15)