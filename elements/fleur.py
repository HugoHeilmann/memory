import util
import turtle
import time

def fleur(t, petal_color):
    t.speed(100)

    # Contour noir
    t.down()
    util.row_right_squares(t, 15)
    t.backward(20)
    t.left(90)
    util.row_right_squares(t, 2)
    util.left_square(t)
    t.forward(20)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 4)
    t.left(90)
    util.left_square(t)
    t.forward(20)
    util.row_right_squares(t, 1)
    t.right(90)
    util.row_left_squares(t, 3)
    t.right(90)
    util.row_right_squares(t, 2)
    t.left(90)
    util.left_square(t)
    t.forward(20)
    util.row_right_squares(t, 3)
    util.left_square(t)
    t.forward(20)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 2)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(60)
    util.right_square(t)
    t.forward(40)
    t.right(90)
    t.backward(20)
    util.row_right_squares(t, 6)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(40)
    t.right(90)
    util.row_right_squares(t, 1)
    util.row_left_squares(t, 1)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 4)
    util.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 1)
    util.row_left_squares(t, 1)
    t.left(90)
    t.forward(20)
    t.right(90)
    util.row_left_squares(t, 1)
    util.row_right_squares(t, 1)
    t.right(90)
    t.forward(40)
    t.left(90)
    util.row_left_squares(t, 1)
    util.row_right_squares(t, 2)
    util.row_left_squares(t, 1)
    t.left(90)
    t.forward(40)
    t.right(90)
    util.row_right_squares(t, 1)
    util.row_left_squares(t, 1)
    util.row_right_squares(t, 1)
    t.right(90)
    t.forward(20)
    t.left(90)
    util.right_square(t)
    t.forward(40)
    t.left(90)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 4)
    util.left_square(t)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    util.left_square(t)
    t.forward(20)
    util.row_right_squares(t, 2)

    # Encrage des pétales
    t.color(petal_color)
    t.begin_fill()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.end_fill()

    # Yeux
    t.up()
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.color("black")
    t.down()
    util.row_right_squares(t, 1)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 1)
    t.up()
    t.forward(20)
    t.down()
    util.row_right_squares(t, 1)
    util.row_left_squares(t, 2)
    util.row_right_squares(t, 1)

    # Pied droit
    t.up()
    t.right(90)
    t.forward(140)
    t.left(90)
    t.color("#0BC600")
    t.down()
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.end_fill()

    # Corps
    t.up()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.down()
    util.row_left_squares(t, 2)
    t.backward(40)
    util.row_right_squares(t, 3)

    # Pied gauche
    t.up()
    t.right(90)
    t.forward(40)
    t.down()
    util.row_left_squares(t, 5)
    t.left(180)
    util.row_left_squares(t, 5)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    util.row_right_squares(t, 3)

    time.sleep(5)

t = turtle.Turtle()
fleur(t, "#F56000")