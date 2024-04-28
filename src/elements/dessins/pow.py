import usefull

def pow(t, type_color, pixel_size):
    t.speed(100)

    if type_color == 1:
        main_color = "#00008B"
        border_color = "#6495ED"
    else:
        main_color = "#CC0000"
        border_color = "#B22222"

    # Fond
    t.begin_fill()
    for _ in range (4):
        t.forward(18*pixel_size)
        t.left(90)
    t.end_fill()

    # Bordure
    t.left(90)
    t.forward(4*pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.right(90)
    t.color(border_color)
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 14, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.up()
    t.forward(10*pixel_size)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 14, pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)

    # Bleu principal
    t.left(90)
    t.color(main_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(14*pixel_size)
        t.left(90)
        t.forward(2*pixel_size)
        t.left(90)
    t.end_fill()
    t.up()
    t.right(90)
    t.forward(12*pixel_size)
    t.left(90)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(14*pixel_size)
        t.left(90)
        t.forward(2*pixel_size)
        t.left(90)
    t.end_fill()

    # P
    t.up()
    t.color("#FFFFFF")
    t.left(90)
    t.forward(3*pixel_size)
    t.down()
    usefull.row_left_squares(t, 8, pixel_size)
    t.backward(8*pixel_size)
    usefull.row_right_squares(t, 8, pixel_size)
    t.backward(pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 4, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)

    # O
    t.up()
    t.left(180)
    t.forward(5*pixel_size)
    t.left(90)
    t.backward(2*pixel_size)
    usefull.row_left_squares(t, 6, pixel_size)
    t.backward(7*pixel_size)
    usefull.row_right_squares(t, 8, pixel_size)
    t.backward(pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 6, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)

    # W
    t.up()
    t.left(180)
    t.forward(4*pixel_size)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 5, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 7, pixel_size)
    t.up()
    t.right(90)
    t.forward(3*pixel_size)
    t.right(90)
    t.down()
    usefull.row_right_squares(t, 6, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 6, pixel_size)