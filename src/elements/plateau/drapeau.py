import usefull
import turtle
import time

def drapeau(t, pixel_size):
    t.speed(100)
    
    # Base
    t.color("#66FF66")
    t.begin_fill()
    for _ in range(2):
        t.forward(4*pixel_size)
        t.left(90)
        t.forward(232*pixel_size)
        t.left(90)
    t.end_fill()
    
    # Bille
    t.left(90)
    t.forward(232*pixel_size)
    t.color("#000000")
    t.forward(pixel_size)
    t.right(90)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)

    t.left(90)
    t.forward(pixel_size)
    t.color("#00CC00")
    t.begin_fill()
    for _ in range(4):
        t.forward(6*pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    t.end_fill()

    # Flag
    t.up()
    t.forward(2*pixel_size)
    usefull.double_right_linear_traverse(t, pixel_size)
    t.color("#000000")
    t.down()
    t.begin_fill()
    t.forward(25*pixel_size)
    t.left(90)
    for _ in range(25):
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.left(180)
    t.forward(25*pixel_size)
    t.end_fill()

    # Tête de mort
    t.left(90)
    t.forward(3*pixel_size)
    t.left(90)
    t.forward(3*pixel_size)
    t.right(90)
    t.color("#00CC00")
    usefull.row_left_squares(t, 9, pixel_size)
    t.backward(8*pixel_size)
    usefull.row_right_squares(t, 7, pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    t.forward(pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.left(90)
        t.forward(6*pixel_size)
        t.left(90)
        t.forward(9*pixel_size)
    t.end_fill()
    t.left(90)
    t.forward(6*pixel_size)
    t.left(90)
    t.forward(3*pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.color("#FFFFFF")
    t.right(90)
    t.backward(2*pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.up()
    t.forward(2*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.up()
    t.right(90)
    t.forward(5*pixel_size)
    t.right(90)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)

t = turtle.Turtle()
t.goto(-200, -200)
drapeau(t, 2)
time.sleep(5)