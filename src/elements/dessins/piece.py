import usefull

def piece(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        color = "#FFD700"
    else:
        color = "#B22222"

    # Contour noir
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 8, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 4, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 8, pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)

    # Encrage
    t.color(color)
    t.begin_fill()
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(8*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(4*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.forward(8*pixel_size)
    usefull.long_left_diagonal(t, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.end_fill()

    # Coeur
    usefull.double_walk_along_up_square_left(t, pixel_size)
    t.forward(pixel_size)
    t.color("#000000")
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 8, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 8, pixel_size)