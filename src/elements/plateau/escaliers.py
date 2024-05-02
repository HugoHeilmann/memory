import usefull

def escaliers(t, pixel_size):
    t.speed(100)

    # Fond marron
    t.color("#B44104") # Caramel
    t.begin_fill()
    for _ in range(4):
        t.forward(23*pixel_size)
        t.left(90)
    t.end_fill()

    # Partie inférieure
    t.begin_fill()
    t.color("#000000")
    t.forward(21*pixel_size)
    t.left(90)
    for _ in range(2):
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(12*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    t.right(90)
    usefull.low_traverse(t, pixel_size)
    t.end_fill()

    # Partie droite
    t.up()
    t.left(90)
    t.forward(23*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.down()
    t.begin_fill()
    t.forward(22*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(13*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.end_fill()

    # Partie supérieure
    t.up()
    t.left(90)
    t.forward(22*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.color("#F4B99A")
    t.down()
    t.begin_fill()
    t.forward(20*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(12*pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.end_fill()

    # Partie gauche
    t.up()
    t.left(90)
    t.forward(21*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.down()
    t.begin_fill()
    t.forward(21*pixel_size)
    t.left(90)
    usefull.low_traverse(t, pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    t.forward(13*pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    usefull.low_traverse(t, pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    t.end_fill()