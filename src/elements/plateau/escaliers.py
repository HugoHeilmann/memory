from usefull.usefull import *


def escaliers(t, pixel_size):
    t.speed(100)

    # Fond marron
    t.color("#BC410D")  # Caramel
    t.begin_fill()
    for _ in range(4):
        t.forward(23 * pixel_size)
        t.left(90)
    t.end_fill()

    # Partie inférieure
    t.begin_fill()
    t.color("#000000")
    t.forward(21 * pixel_size)
    t.left(90)
    for _ in range(2):
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    walk_along_up_square_left(t, pixel_size)
    long_left_diagonal_from_above(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(12 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.right(90)
    low_traverse(t, pixel_size)
    t.end_fill()

    # Partie droite
    t.up()
    t.left(90)
    t.forward(23 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.down()
    t.begin_fill()
    t.forward(22 * pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(13 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.end_fill()

    # Partie supérieure
    t.up()
    t.left(90)
    t.forward(22 * pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    t.color("#F5ADAE")
    t.down()
    t.begin_fill()
    t.forward(20 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(90)
    t.forward(2 * pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(12 * pixel_size)
    walk_along_up_square_left(t, pixel_size)
    low_traverse(t, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.end_fill()

    # Partie gauche
    t.up()
    t.left(90)
    t.forward(21 * pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.down()
    t.begin_fill()
    t.forward(21 * pixel_size)
    t.left(90)
    low_traverse(t, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(13 * pixel_size)
    walk_along_up_square_left(t, pixel_size)
    low_traverse(t, pixel_size)
    double_walk_along_up_square_right(t, pixel_size)
    t.forward(2 * pixel_size)
    t.right(90)
    long_left_diagonal_from_above(t, pixel_size)
    t.end_fill()
