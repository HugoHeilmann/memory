import usefull

def etoile(t, color):
    t.speed(100)

    # Contour noir
    usefull.row_right_squares(t, 3)
    usefull.row_left_squares(t, 2)
    usefull.double_walk_along_up_square_left(t)
    usefull.row_right_squares(t, 2)
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 2)
    t.right(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 3)
    t.backward(20)
    t.left(90)
    usefull.row_right_squares(t, 1)
    usefull.row_left_squares(t, 2)
    usefull.double_walk_along_up_square_left(t)
    usefull.row_right_squares(t, 2)
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 1)
    t.right(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 1)
    usefull.row_right_squares(t, 2)
    t.left(90)
    usefull.row_left_squares(t, 4)
    t.forward(20)
    t.right(90)
    usefull.row_right_squares(t, 2)
    usefull.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t ,2)
    t.right(90)
    t.forward(20)
    usefull.row_left_squares(t, 5)
    t.left(90)
    t.forward(20)
    for _ in range(4):
        usefull.left_square(t)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
    t.right(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 2)
    t.right(90)
    t.forward(20)
    usefull.left_square(t)

    # Encrage
    t.color(color)
    t.left(90)
    t.begin_fill()
    t.forward(20)
    t.left(90)
    t.forward(40)
    usefull.long_left_diagonal(t)
    usefull.long_left_diagonal(t)
    usefull.walk_along_up_square_left(t)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    t.left(90)
    usefull.low_traverse(t)
    t.right(90)
    t.forward(40)
    usefull.long_left_diagonal(t)
    usefull.walk_along_up_square_left(t)
    t.forward(20)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    usefull.low_traverse(t)
    t.left(90)
    t.forward(80)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    t.forward(40)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    t.forward(80)
    t.left(90)
    usefull.low_traverse(t)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    usefull.low_traverse(t)
    t.right(90)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.end_fill()

    # Yeux
    t.up()
    t.left(180)
    t.forward(120)
    t.left(90)
    t.forward(100)
    t.color("#000000")
    t.down()
    usefull.row_left_squares(t, 3)
    t.up()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.down()
    usefull.row_left_squares(t, 3)