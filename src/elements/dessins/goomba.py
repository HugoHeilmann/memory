from usefull.usefull import *


def goomba(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        body_color = "#8B4513"
    else:
        body_color = "#FFD700"

    # Pieds
    t.color("#000000")
    row_left_squares(t, 2, pixel_size)
    t.backward(3 * pixel_size)
    row_right_squares(t, 5, pixel_size)
    t.backward(5 * pixel_size)
    t.right(90)
    t.forward(2 * pixel_size)
    t.left(90)
    row_left_squares(t, 6, pixel_size)
    t.backward(5 * pixel_size)
    row_right_squares(t, 5, pixel_size)
    t.up()
    t.forward(2 * pixel_size)
    t.down()
    row_right_squares(t, 3, pixel_size)
    t.backward(2 * pixel_size)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    right_square(t, pixel_size)
    t.forward(pixel_size)
    left_square(t, pixel_size)
    right_square(t, pixel_size)

    # Corps
    t.left(90)
    t.forward(pixel_size)
    t.color("#FFC992")
    row_right_squares(t, 5, pixel_size)
    t.backward(4 * pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.right(90)
    t.forward(2 * pixel_size)
    t.left(90)
    t.forward(3 * pixel_size)
    t.left(180)
    row_right_squares(t, 8, pixel_size)
    t.backward(8 * pixel_size)
    row_left_squares(t, 8, pixel_size)
    t.left(90)
    low_traverse(t, pixel_size)
    row_right_squares(t, 6, pixel_size)

    # Corps
    t.up()
    t.forward(5 * pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.right(90)
    t.color(body_color)
    t.down()
    row_left_squares(t, 16, pixel_size)
    t.left(180)
    t.forward(pixel_size)
    row_left_squares(t, 4, pixel_size)
    t.forward(6 * pixel_size)
    row_left_squares(t, 4, pixel_size)
    t.forward(pixel_size)
    double_right_linear_traverse(t, pixel_size)
    row_right_squares(t, 16, pixel_size)
    t.backward(16 * pixel_size)
    row_left_squares(t, 16, pixel_size)
    t.up()
    t.left(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.down()
    row_right_squares(t, 14, pixel_size)
    t.backward(14 * pixel_size)
    row_left_squares(t, 14, pixel_size)
    t.up()
    double_right_linear_traverse(t, pixel_size)
    t.forward(pixel_size)
    row_right_squares(t, 12, pixel_size)
    t.backward(11 * pixel_size)
    row_left_squares(t, 10, pixel_size)
    t.up()
    t.left(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.down()
    row_left_squares(t, 8, pixel_size)
    t.backward(7 * pixel_size)
    row_right_squares(t, 6, pixel_size)
    t.backward(5 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_right_squares(t, 4, pixel_size)

    # Yeux
    t.left(90)
    t.forward(6 * pixel_size)
    t.color("#FFFFFF")
    row_left_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 4, pixel_size)
    t.up()
    t.right(90)
    t.forward(7 * pixel_size)
    t.right(90)
    t.down()
    row_left_squares(t, 4, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)
    t.right(90)
    row_right_squares(t, 2, pixel_size)

    # Sourcils + pupilles
    t.up()
    t.forward(2 * pixel_size)
    t.right(90)
    t.forward(4 * pixel_size)
    t.left(180)
    t.color("#000000")
    t.down()
    row_right_squares(t, 2, pixel_size)
    t.left(90)
    row_right_squares(t, 2, pixel_size)
    right_square(t, pixel_size)
    t.right(90)
    row_right_squares(t, 5, pixel_size)
    left_square(t, pixel_size)
    t.right(90)
    row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    row_right_squares(t, 2, pixel_size)
