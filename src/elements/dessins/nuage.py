from usefull.usefull import *


def nuage(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        body_color = "#FFFFFF"
        reflect_color = "#D3D3D3"
        eyes_color = "#000000"
    else:
        body_color = "#000000"
        reflect_color = "#696969"
        eyes_color = "#FFFF00"

    # Contour noir
    row_right_squares(t, 4, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 4, pixel_size)
    left_square(t, pixel_size)
    low_traverse(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 3, pixel_size)
    row_right_squares(t, 6, pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 1, pixel_size)
    row_right_squares(t, 10, pixel_size)
    row_left_squares(t, 1, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 3, pixel_size)
    row_right_squares(t, 6, pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    right_square(t, pixel_size)

    # Reflet
    t.color(reflect_color)
    row_left_squares(t, 1, pixel_size)
    row_right_squares(t, 4, pixel_size)
    row_left_squares(t, 2, pixel_size)
    row_right_squares(t, 4, pixel_size)
    t.left(90)
    left_square(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    row_left_squares(t, 4, pixel_size)
    t.backward(pixel_size)
    row_right_squares(t, 6, pixel_size)
    row_left_squares(t, 3, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    right_square(t, pixel_size)

    # Encrage
    t.color(body_color)
    t.begin_fill()
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(9 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(3 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(6 * pixel_size)
    long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(4 * pixel_size)
    long_left_diagonal(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(3 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(3 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(5 * pixel_size)
    walk_along_up_square_left(t, pixel_size)
    t.forward(3 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.end_fill()

    # Yeux
    t.up()
    t.forward(3 * pixel_size)
    t.left(90)
    t.forward(3 * pixel_size)
    t.color(eyes_color)
    t.down()
    row_left_squares(t, 3, pixel_size)
    t.up()
    t.right(90)
    t.forward(3 * pixel_size)
    t.right(90)
    t.down()
    row_right_squares(t, 3, pixel_size)

    # Bouche
    t.up()
    t.backward(6 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(180)
    t.down()
    row_left_squares(t, 1, pixel_size)
    row_right_squares(t, 4, pixel_size)
    row_left_squares(t, 1, pixel_size)
