from usefull.usefull import *


def bloc(t, pixel_size):
    t.speed(100)

    # Fond noir
    t.begin_fill()
    for _ in range(4):
        t.forward(12 * pixel_size)
        for _ in range(2):
            t.right(90)
            t.forward(pixel_size)
            t.left(90)
            t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Bordure
    t.forward(12 * pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.color("#754E17")
    row_right_squares(t, 1, pixel_size)
    row_left_squares(t, 12, pixel_size)
    t.right(90)
    row_right_squares(t, 1, pixel_size)
    t.backward(pixel_size)
    row_left_squares(t, 12, pixel_size)
    row_right_squares(t, 1, pixel_size)

    # Fond jaune foncé
    t.right(90)
    t.forward(pixel_size)
    t.color("#B3842E")
    t.begin_fill()
    for _ in range(4):
        t.forward(11 * pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Fond jaune clair
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.color("#F2C31F")
    t.begin_fill()
    for _ in range(4):
        t.forward(9 * pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Reflets blanc
    t.forward(5 * pixel_size)
    t.color("white")
    row_left_squares(t, 1, pixel_size)
    t.up()
    t.forward(pixel_size)
    t.down()
    row_left_squares(t, 3, pixel_size)
    t.right(90)
    row_right_squares(t, 1, pixel_size)
    t.backward(pixel_size)
    row_left_squares(t, 3, pixel_size)

    # ?
    t.backward(pixel_size)
    t.color("black")
    row_right_squares(t, 7, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.right(90)
    row_left_squares(t, 3, pixel_size)
    row_right_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    for _ in range(2):
        row_left_squares(t, 2, pixel_size)
        t.right(90)
        row_left_squares(t, 3, pixel_size)
        t.right(90)
    from_above(t, pixel_size)
    t.forward(pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.right(90)
    row_left_squares(t, 3, pixel_size)
    t.left(180)
    row_left_squares(t, 6, pixel_size)
    t.right(90)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 1, pixel_size)

    # Plein blanc
    t.backward(pixel_size)
    t.right(90)
    t.color("white")
    row_right_squares(t, 1, 2 * pixel_size)
    t.left(90)
    row_left_squares(t, 1, pixel_size)
    t.backward(3 * pixel_size)
    row_right_squares(t, 1, pixel_size)
    t.right(90)
    row_left_squares(t, 3, 2 * pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 1, 2 * pixel_size)
    t.backward(2 * pixel_size)
    t.left(90)
    for i in range(2):
        row_left_squares(t, 1, 2 * pixel_size)
        if i != 1:
            t.backward(pixel_size)
    t.up()
    t.left(90)
    t.forward(3 * pixel_size)
    t.left(90)
    t.down()
    for i in range(2):
        row_right_squares(t, 1, 2 * pixel_size)
        if i != 1:
            t.backward(pixel_size)
