import usefull

def boo(t, body_color, mouth_color):
    t.speed(100)

    # Contour noir
    usefull.row_right_squares(t, 4)
    usefull.row_left_squares(t, 2)
    usefull.double_walk_along_up_square_left(t)
    usefull.row_right_squares(t, 2)
    usefull.left_square(t)
    t.forward(20)
    t.left(90)
    t.forward(20)
    usefull.row_right_squares(t, 3)
    usefull.row_left_squares(t, 3)
    usefull.double_walk_along_up_square_left(t)
    usefull.row_right_squares(t, 2)
    usefull.left_square(t)
    usefull.long_left_diagonal(t)
    t.left(90)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 5)
    usefull.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 2)
    usefull.row_right_squares(t, 5)
    usefull.row_left_squares(t, 2)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    usefull.row_right_squares(t, 3)

    # Encrage du corps
    t.color(body_color)
    t.begin_fill()
    usefull.walk_along_up_square_right(t)
    t.forward(80)
    usefull.long_left_diagonal(t)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(60)
    usefull.walk_along_up_square_left(t)
    t.forward(60)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(100)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(40)
    usefull.walk_along_up_square_right(t)
    t.forward(100)
    usefull.long_left_diagonal(t)
    t.left(90)
    t.forward(20)
    usefull.walk_along_up_square_right(t)
    t.forward(60)
    t.end_fill()

    # Yeux
    t.up()
    t.color("black")
    t.left(90)
    t.forward(140)
    t.down()
    usefull.row_left_squares(t, 2)
    t.up()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.down()
    usefull.row_right_squares(t, 2)

    # Main
    t.up()
    t.left(90)
    t.forward(100)
    t.down()
    usefull.right_square(t)
    t.forward(20)
    usefull.row_left_squares(t, 2)
    t.right(90)
    usefull.row_left_squares(t, 2)
    usefull.right_square(t)

    # Bouche
    t.up()
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.down()
    t.color(mouth_color)
    usefull.row_left_squares(t, 5)
    t.left(180)
    usefull.row_left_squares(t, 5)
    t.right(90)
    t.forward(40)
    usefull.left_square(t)
    t.left(90)
    t.forward(20)
    t.left(180)
    usefull.row_right_squares(t, 5)
    t.left(90)
    usefull.left_square(t)
    t.left(90)
    t.forward(40)
    usefull.right_square(t)
    t.forward(20)
    t.left(90)
    t.forward(60)
    usefull.right_square(t)
    t.left(90)
    t.forward(20)
    usefull.right_square(t)
    t.forward(40)
    usefull.right_square(t)