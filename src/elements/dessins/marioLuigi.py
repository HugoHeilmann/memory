import usefull

def mario_luigi(t, clothes_color):
    t.speed(100)

    # Chaussures
    t.color("#663300")
    usefull.row_right_squares(t, 4)
    t.backward(60)
    usefull.row_left_squares(t, 3)
    t.up()
    t.forward(80)
    t.down()
    usefull.row_left_squares(t, 3)
    t.backward(60)
    usefull.row_right_squares(t, 4)

    # Salopette
    t.up()
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.color("#000077")
    t.down()
    usefull.row_left_squares(t, 3)
    t.forward(40)
    usefull.row_left_squares(t, 3)
    t.left(180)
    usefull.row_left_squares(t, 8)
    t.left(90)
    usefull.low_traverse(t)
    usefull.row_right_squares(t, 6)
    t.right(90)
    t.forward(20)
    t.right(90)
    usefull.row_left_squares(t, 1)
    t.forward(20)
    usefull.row_left_squares(t, 2)
    t.forward(20)
    usefull.left_square(t)
    t.left(90)
    t.forward(20)
    t.left(90)
    usefull.row_right_squares(t, 4)
    t.right(90)
    usefull.row_right_squares(t, 3)
    t.backward(40)
    t.right(90)
    t.forward(60)
    usefull.left_square(t)

    # Boutons
    t.up()
    t.right(90)
    t.forward(20)
    t.color("#FFFF00")
    t.down()
    usefull.left_square(t)
    t.up()
    t.right(90)
    t.forward(40)
    t.down()
    usefull.left_square(t)

    # Mains
    t.up()
    t.forward(60)
    t.color("#FFA07A")
    t.down()
    usefull.row_left_squares(t, 2)
    t.left(90)
    t.forward(40)
    t.left(90)
    usefull.row_right_squares(t, 2)
    t.backward(40)
    usefull.row_left_squares(t, 3)
    t.up()
    t.forward(120)
    t.down()
    usefull.row_left_squares(t, 3)
    t.backward(40)
    usefull.row_right_squares(t, 2)
    t.left(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 2)

    # T-shirt
    t.color(clothes_color)
    usefull.left_square(t)
    t.backward(40)
    usefull.walk_along_up_square_right(t)
    usefull.row_left_squares(t, 4)
    t.backward(60)
    usefull.row_right_squares(t, 3)
    t.up()
    t.forward(20)
    t.down()
    usefull.row_right_squares(t, 2)
    t.up()
    usefull.low_traverse(t)
    t.right(90)
    t.down()
    usefull.row_right_squares(t, 1)
    usefull.left_square(t)
    usefull.row_right_squares(t, 3)
    t.backward(80)
    t.right(90)
    t.forward(40)
    t.left(90)
    usefull.row_left_squares(t, 3)
    t.backward(60)
    usefull.row_right_squares(t, 2)
    t.left(180)
    t.up()
    t.forward(60)
    t.down()
    usefull.row_left_squares(t, 3)

    # Visage
    t.up()
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.color("#FFA07A")
    t.down()
    usefull.row_left_squares(t, 7)
    t.right(90)
    t.forward(20)
    usefull.row_left_squares(t, 2)
    t.backward(40)
    t.right(90)
    usefull.row_right_squares(t, 4)
    t.backward(40)
    usefull.row_left_squares(t, 3)
    t.up()
    t.forward(20)
    usefull.row_left_squares(t, 3)
    t.up()
    t.left(90)
    usefull.long_left_diagonal_from_above(t)
    t.down()
    usefull.row_left_squares(t, 2)
    usefull.left_square(t)
    usefull.right_square(t)
    t.forward(20)
    ### Yeux ###
    t.color("#000000")
    usefull.left_square(t)
    usefull.right_square(t)
    t.forward(20)
    ### End ###
    t.color("#FFA07A")
    usefull.row_left_squares(t, 3)
    t.backward(60)
    usefull.row_right_squares(t, 2)

    # Pilosité
    t.color("#663300")
    usefull.row_right_squares(t, 3)
    t.left(90)
    usefull.row_right_squares(t, 3)
    t.left(90)
    usefull.row_left_squares(t, 1)
    t.up()
    t.forward(80)
    t.down()
    usefull.row_left_squares(t, 4)
    t.backward(60)
    t.left(90)
    usefull.row_right_squares(t, 2)
    t.up()
    t.left(90)
    t.forward(60)
    t.down()
    usefull.row_left_squares(t, 2)
    t.right(90)
    usefull.row_right_squares(t, 2)

    # Casquette
    t.color(clothes_color)
    usefull.row_left_squares(t, 1)
    t.right(90)
    usefull.row_left_squares(t, 5)
    t.backward(100)
    usefull.row_right_squares(t, 8)    