def low_traverse(t):
    t.forward(20)
    t.left(90)
    t.forward(20)

def long_left_diagonal_from_above(t):
    t.forward(40)
    t.left(90)
    t.forward(20)

def from_above(t):
    t.right(90)
    t.forward(60)
    t.right(90)

def walk_along_up_square(t):
    t.right(90)
    t.forward(20)
    t.left(90)

def long_left_diagonal(t):
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(40)

def double_high_traverse(t):
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)

def double_right_linear_traverse(t):
    t.right(90)
    t.forward(40)
    t.right(90)

def left_square(t):
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()

def right_square(t):
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.right(90)
    t.end_fill()

def row_left_squares(t, number):
    t.down()
    t.begin_fill()
    for _ in range(number):
        left_square(t)
        t.forward(20)
    t.end_fill()

def row_right_squares(t, number):
    t.down()
    t.begin_fill()
    for _ in range(number):
        right_square(t)
        t.forward(20)
    t.end_fill()