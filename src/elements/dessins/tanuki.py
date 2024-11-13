from usefull.usefull import *


def tanuki(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        main_color = "#8B4513"
        veins_color = "#000000"
    else:
        main_color = "#FFFFFF"
        veins_color = "#FFFF00"

    # Contour noir
    t.color("#000000")
    row_left_squares(t, 3, pixel_size)
    row_right_squares(t, 5, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    for _ in range(2):
        row_right_squares(t, 1, pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 3, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 2, pixel_size)
    t.left(90)
    row_right_squares(t, 1, pixel_size)
    t.left(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    row_left_squares(t, 4, pixel_size)
    double_walk_along_up_square_left(t, pixel_size)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    for _ in range(3):
        row_right_squares(t, 1, pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    left_square(t, pixel_size)
    right_square(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_right_squares(t, 2, pixel_size)
    t.left(90)
    row_right_squares(t, 2, pixel_size)

    # Encrage
    t.color(main_color)
    t.begin_fill()
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(5 * pixel_size)
    long_left_diagonal(t, pixel_size)
    for _ in range(2):
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(3 * pixel_size)
    long_left_diagonal(t, pixel_size)
    t.left(90)
    low_traverse(t, pixel_size)
    t.right(90)
    t.forward(4 * pixel_size)

    for _ in range(2):
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        t.forward(2 * pixel_size)
    for _ in range(2):
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
    double_walk_along_up_square_left(t, pixel_size)
    long_left_diagonal_from_above(t, pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    t.end_fill()

    # Veines
    t.left(90)
    t.forward(3 * pixel_size)
    t.right(90)
    t.color(veins_color)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(2 * pixel_size)
    right_square(t, pixel_size)
    t.left(180)
    row_right_squares(t, 3, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(2 * pixel_size)
    right_square(t, pixel_size)
    t.left(180)
    row_right_squares(t, 4, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    row_left_squares(t, 2, pixel_size)

    # Queue
    t.up()
    t.left(90)
    t.forward(2 * pixel_size)
    t.color(main_color)
    t.down()
    row_right_squares(t, 2, pixel_size)
