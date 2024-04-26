def low_traverse(t, pixel_size):
    t.forward(pixel_size)
    t.left(90)
    t.forward(pixel_size)

def long_left_diagonal_from_above(t, pixel_size):
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(pixel_size)

def from_above(t, pixel_size):
    t.right(90)
    t.forward(3*pixel_size)
    t.right(90)

def walk_along_up_square_right(t, pixel_size):
    t.right(90)
    t.forward(pixel_size)
    t.left(90)

def double_walk_along_up_square_right(t, pixel_size):
    t.right(90)
    t.forward(2*pixel_size)
    t.left(90)

def walk_along_up_square_left(t, pixel_size):
    t.left(90)
    t.forward(pixel_size)
    t.right(90)

def double_walk_along_up_square_left(t, pixel_size):
    t.left(90)
    t.forward(2*pixel_size)
    t.right(90)

def long_left_diagonal(t, pixel_size):
    t.left(90)
    t.forward(pixel_size)
    t.right(90)
    t.forward(2*pixel_size)

def double_high_traverse(t, pixel_size):
    t.forward(pixel_size)
    double_walk_along_up_square_right(t, pixel_size)

def double_right_linear_traverse(t, pixel_size):
    t.right(90)
    t.forward(2*pixel_size)
    t.right(90)

def left_square(t, pixel_size):
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(pixel_size)
        t.left(90)
    t.end_fill()

def right_square(t, pixel_size):
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

def row_left_squares(t, number, pixel_size):
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(pixel_size*number)
        t.left(90)
        t.forward(pixel_size)
        t.left(90)
    t.end_fill()
    t.forward(pixel_size*number)

def row_right_squares(t, number, pixel_size):
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(pixel_size*number)
        t.right(90)
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()
    t.forward(pixel_size*number)