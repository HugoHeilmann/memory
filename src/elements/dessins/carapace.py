from usefull.usefull import *


def carapace(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        main_color = "#32CD32"
    else:
        main_color = "#DC143C"

    # Contour noir
    left_square(t, pixel_size)
    row_right_squares(t, 1, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 1, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 4, pixel_size)
    row_left_squares(t, 2, pixel_size)
    double_walk_along_up_square_left(t, pixel_size)
    row_right_squares(t, 1, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    row_right_squares(t, 5, pixel_size)
    t.backward(pixel_size)
    row_left_squares(t, 3, pixel_size)
    double_walk_along_up_square_left(t, pixel_size)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    row_right_squares(t, 6, pixel_size)
    t.backward(pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 1, pixel_size)
    row_right_squares(t, 2, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.backward(pixel_size)
    row_right_squares(t, 3, pixel_size)
    t.left(90)
    row_left_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    row_right_squares(t, 3, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    row_right_squares(t, 1, pixel_size)
    t.left(90)
    row_right_squares(t, 6, pixel_size)
    t.left(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 3, pixel_size)
    t.backward(pixel_size)
    row_left_squares(t, 2, pixel_size)

    # Bordure blanche
    t.color("#FFFFFF")
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 3, pixel_size)
    t.left(90)
    left_square(t, pixel_size)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 4, pixel_size)
    t.backward(4 * pixel_size)
    row_right_squares(t, 6, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    right_square(t, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    row_left_squares(t, 3, pixel_size)
    t.right(90)
    row_right_squares(t, 1, pixel_size)

    # Encrage
    t.up()
    t.forward(2 * pixel_size)
    t.right(90)
    t.color(main_color)
    t.down()
    t.begin_fill()
    t.forward(14 * pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    t.forward(6 * pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.end_fill()
    t.right(90)
    t.forward(pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.forward(12 * pixel_size)
        t.left(90)
        t.forward(3 * pixel_size)
        t.left(90)
    t.end_fill()
    t.forward(pixel_size)
    t.left(90)
    t.forward(3 * pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.forward(2 * pixel_size)
        t.right(90)
        t.forward(10 * pixel_size)
        t.right(90)
    t.end_fill()
    t.forward(2 * pixel_size)
    t.right(90)
    t.forward(pixel_size)
    row_left_squares(t, 8, pixel_size)
    t.left(180)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_right_squares(t, 4, pixel_size)

    # Craquelures
    t.left(180)
    t.color("#000000")
    row_right_squares(t, 4, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    for _ in range(4):
        row_left_squares(t, 1, pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.up()
    t.right(90)
    t.forward(2 * pixel_size)
    t.down()
    row_right_squares(t, 1, pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    left_square(t, pixel_size)
    t.right(90)
    row_right_squares(t, 4, pixel_size)
    left_square(t, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    for _ in range(2):
        row_left_squares(t, 1, pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.left(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.left(180)
    for _ in range(4):
        row_right_squares(t, 1, pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
