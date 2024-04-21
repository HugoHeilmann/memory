def low_traverse(turtle):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)

def walk_along_up_square(turtle):
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

def long_left_diagonal(turtle):
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)

def double_high_traverse(turtle):
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)

def double_right_linear_traverse(turtle):
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)

def mid_left_square(turtle):
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)

def left_square(turtle):
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()

def right_square(turtle):
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

def row_left_squares(turtle, number):
    turtle.down()
    turtle.begin_fill()
    for i in range(number):
        left_square(turtle)
        turtle.forward(20)
    turtle.end_fill()

def row_right_squares(turtle, number):
    turtle.down()
    turtle.begin_fill()
    for i in range(number):
        right_square(turtle)
        turtle.forward(20)
    turtle.end_fill()