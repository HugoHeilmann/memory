import turtle
import random
import time
import usefull

### TEMPORAIRE ###

## TOUTES LES FONCTIONS POUR LE PLATEAU DE JEU ##

def buisson(t, pixel_size) :
    # Contour noir
    t.color("black")
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 5, pixel_size)
    t.backward(5*pixel_size)
    usefull.row_right_squares(t, 5, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    usefull.row_left_squares(t, 1, 2*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_right_squares(t, 1, 2*pixel_size)
    t.left(180)
    t.forward(3*pixel_size)

    # Remplissage vert
    t.color("#82DF15")
    t.left(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(2*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.forward(3*pixel_size)
        t.left(90)
        t.forward(5*pixel_size)
        t.left(90)
    t.end_fill()
    t.left(90)
    t.forward(3*pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(180)
    usefull.row_right_squares(t, 5, pixel_size)

def colline(t, pixel_size):
    # Contour noir
    t.color("black")
    for i in range(3):
        usefull.row_left_squares(t, 1, pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        for _ in range(3-i):
            usefull.row_left_squares(t, 2, pixel_size)
            t.left(90)
            t.forward(pixel_size)
            usefull.row_right_squares(t, 2, pixel_size)
            t.right(90)
            t.forward(pixel_size)

    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 3, pixel_size)
    usefull.row_left_squares(t, 5, pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.left(90)
    for i in range(3):
        for _ in range(i+1):
            t.right(90)
            usefull.row_left_squares(t, 2, pixel_size)
            t.left(90)
            t.forward(pixel_size)
            usefull.row_right_squares(t, 2, pixel_size)
            t.right(90)
            t.forward(pixel_size)
            t.left(90)
        usefull.row_right_squares(t, 1, pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)

    # Remplissage vert
    t.left(180)
    t.forward(pixel_size)
    t.color("#0CC404")
    t.begin_fill()
    t.forward(60*pixel_size)
    t.right(180)
    t.begin_fill()
    for i in range(3):
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        for _ in range(3-i):
            t.forward(2*pixel_size)
            t.left(90)
            t.forward(pixel_size)
            t.right(90)
            t.forward(pixel_size)
            t.left(90)
            t.forward(2*pixel_size)
            t.right(90)
    for _ in range(2):
        t.forward(2*pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.forward(3*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.right(90)
    t.forward(5*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.left(90)
    t.forward(3*pixel_size)
    for _ in range(2):
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(2*pixel_size)
    for i in range(3):
        for _ in range(i+1):
            t.right(90)
            t.forward(2*pixel_size)
            t.left(90)
            t.forward(pixel_size)
            t.right(90)
            t.forward(pixel_size)
            t.left(90)
            t.forward(2*pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
    t.end_fill()

    # Trous noirs

    t.backward(32*pixel_size)
    t.left(90)
    t.forward(10*pixel_size)
    t.color("#000000")
    usefull.row_right_squares(t, 1, 3*pixel_size)
    usefull.row_right_squares(t, 1, 3*pixel_size)
    t.up()
    t.right(90)
    t.forward(7*pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    t.left(180)
    t.down()
    usefull.row_right_squares(t, 7, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 9, pixel_size)
    t.backward(pixel_size)
    t.left(180)
    usefull.row_left_squares(t, 7, pixel_size)

def drapeau(t, pixel_size):
    # Base
    t.color("#66FF66")
    t.begin_fill()
    for _ in range(2):
        t.forward(4*pixel_size)
        t.left(90)
        t.forward(232*pixel_size)
        t.left(90)
    t.end_fill()
    
    # Bille
    t.left(90)
    t.forward(232*pixel_size)
    t.color("#000000")
    t.forward(pixel_size)
    t.right(90)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)

    t.left(90)
    t.forward(pixel_size)
    t.color("#00CC00")
    t.begin_fill()
    for _ in range(4):
        t.forward(6*pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
    t.end_fill()

    # Flag
    t.up()
    t.forward(2*pixel_size)
    usefull.double_right_linear_traverse(t, pixel_size)
    t.color("#FFFFFF")
    t.down()
    t.begin_fill()
    t.forward(25*pixel_size)
    t.left(90)
    for _ in range(25):
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.left(180)
    t.forward(25*pixel_size)
    t.end_fill()

    # Tête de mort
    t.left(90)
    t.forward(3*pixel_size)
    t.left(90)
    t.forward(3*pixel_size)
    t.right(90)
    t.color("#00CC00")
    usefull.row_left_squares(t, 9, pixel_size)
    t.backward(8*pixel_size)
    usefull.row_right_squares(t, 7, pixel_size)
    usefull.walk_along_up_square_left(t, pixel_size)
    t.forward(pixel_size)
    t.begin_fill()
    for _ in range(2):
        t.left(90)
        t.forward(6*pixel_size)
        t.left(90)
        t.forward(9*pixel_size)
    t.end_fill()
    t.left(90)
    t.forward(6*pixel_size)
    t.left(90)
    t.forward(3*pixel_size)
    usefull.row_right_squares(t, 3, pixel_size)
    t.left(90)
    usefull.long_left_diagonal_from_above(t, pixel_size)
    t.forward(2*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.color("#FFFFFF")
    t.right(90)
    t.up()
    t.backward(2*pixel_size)
    t.down()
    usefull.row_right_squares(t, 1, pixel_size)
    t.up()
    t.forward(2*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.up()
    t.right(90)
    t.forward(5*pixel_size)
    t.right(90)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)
    t.backward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)

def escaliers(t, pixel_size):
    # Fond marron
    t.color("#BC410D") # Caramel
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
    t.color("#F5ADAE")
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

def sol(t, pixel_size):
    # Fond marron
    t.color("#BB410E") # Caramel
    usefull.row_left_squares(t, 1, 21*pixel_size)
    t.backward(21*pixel_size)

    # Bord inférieur
    t.color("#000000")
    usefull.row_right_squares(t, 9, pixel_size)
    t.color("#B44104")
    usefull.row_right_squares(t, 1, pixel_size)
    t.color("#FBAD97") # Ecru
    usefull.row_right_squares(t, 1, pixel_size)
    t.color("#000000")
    usefull.row_right_squares(t, 10, pixel_size)
    t.color("#B44104")
    usefull.row_right_squares(t, 1, pixel_size)

    # Bord droit
    t.left(90)
    t.color("#000000")
    usefull.row_left_squares(t, 14, pixel_size)
    t.color("#B44104")
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#000000")
    usefull.row_left_squares(t, 6, pixel_size)
    t.color("#B44104")
    usefull.row_left_squares(t, 1, pixel_size)

    # Bord supérieur
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#FBAD97")
    usefull.row_left_squares(t, 6, pixel_size)
    t.color("#B44104")
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#000000")
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#FBAD97")
    usefull.row_left_squares(t, 13, pixel_size)
    t.color("#B44104")
    usefull.row_left_squares(t, 1, pixel_size)

    # Bord gauche
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#FBAD97")
    usefull.row_left_squares(t, 13, pixel_size)
    t.color("#000000")
    usefull.row_left_squares(t, 1, pixel_size)
    t.color("#FBAD97")
    usefull.row_left_squares(t, 7, pixel_size)
    t.color("#B44104")
    usefull.row_left_squares(t, 1, pixel_size)

    # Craquelures
    t.up()
    t.backward(8*pixel_size)
    t.left(90)
    t.forward(pixel_size)
    t.color("#000000")
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 6, pixel_size)
    t.backward(6*pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.forward(pixel_size)
    t.left(90)
    t.backward(5*pixel_size)
    usefull.row_left_squares(t, 6, pixel_size)
    t.backward(6*pixel_size)
    usefull.row_right_squares(t, 6, pixel_size)
    t.right(90)
    t.forward(2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 13, pixel_size)
    t.up()
    t.right(90)
    t.forward(2*pixel_size)
    t.right(90)
    t.forward(4*pixel_size)
    t.down()
    usefull.row_left_squares(t, 3, pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 6, pixel_size)
    t.up()
    t.right(90)
    t.forward(12*pixel_size)
    t.down()
    usefull.row_right_squares(t, 2, pixel_size)

    # Lumière
    t.up()
    t.right(90)
    t.forward(21*pixel_size)
    t.right(90)
    t.forward(6*pixel_size)
    t.right(90)
    t.color("#FBAD97")
    t.down()
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.up()
    t.right(90)
    t.forward(3*pixel_size)
    t.left(90)
    t.down()
    usefull.row_left_squares(t, 6, pixel_size)
    t.up()
    t.forward(3*pixel_size)
    t.right(90)
    t.forward(3*pixel_size)
    t.left(180)
    t.down()
    usefull.row_left_squares(t, 6, pixel_size)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.left(90)
    usefull.row_right_squares(t, 6, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 7, pixel_size)
    t.backward(7*pixel_size)
    t.left(90)
    t.up()
    t.forward(pixel_size)
    t.down()
    usefull.row_right_squares(t, 6, pixel_size)

def bloc(t, pixel_size) :
    t.speed(100)

    # Fond noir
    t.begin_fill()
    for _ in range(4):
        t.forward(12*pixel_size)
        for _ in range(2):
            t.right(90)
            t.forward(pixel_size)
            t.left(90)
            t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Bordure
    t.forward(12*pixel_size)
    t.right(90)
    t.forward(pixel_size)
    t.color("#754E17")
    usefull.row_right_squares(t, 1, pixel_size)
    usefull.row_left_squares(t, 12, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 1, pixel_size)
    t.backward(pixel_size)
    usefull.row_left_squares(t, 12, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)

    # Fond jaune foncé
    t.right(90)
    t.forward(pixel_size)
    t.color("#B3842E")
    t.begin_fill()
    for _ in range(4):
        t.forward(11*pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Fond jaune clair
    t.forward(pixel_size)
    usefull.walk_along_up_square_right(t, pixel_size)
    t.color("#F2C31F")
    t.begin_fill()
    for _ in range(4):
        t.forward(9*pixel_size)
        t.right(90)
        t.forward(pixel_size)
        t.left(90)
        t.forward(pixel_size)
        t.right(90)
    t.end_fill()

    # Reflets blanc
    t.forward(5*pixel_size)
    t.color("white")
    usefull.row_left_squares(t, 1, pixel_size)
    t.up()
    t.forward(pixel_size)
    t.down()
    usefull.row_left_squares(t, 3, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 1, pixel_size)
    t.backward(pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)

    # ?
    t.backward(pixel_size)
    t.color("black")
    usefull.row_right_squares(t, 7, pixel_size)
    usefull.double_walk_along_up_square_right(t, pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 3, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.left(90)
    t.forward(2*pixel_size)
    for _ in range(2):
        usefull.row_left_squares(t, 2, pixel_size)
        t.right(90)
        usefull.row_left_squares(t, 3, pixel_size)
        t.right(90)
    usefull.from_above(t, pixel_size)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 3, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 3, pixel_size)
    t.left(180)
    usefull.row_left_squares(t, 6, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 2, pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)

    # Plein blanc
    t.backward(pixel_size)
    t.right(90)
    t.color("white")
    usefull.row_right_squares(t, 1, 2*pixel_size)
    t.left(90)
    usefull.row_left_squares(t, 1, pixel_size)
    t.backward(3*pixel_size)
    usefull.row_right_squares(t, 1, pixel_size)
    t.right(90)
    usefull.row_left_squares(t, 3, 2*pixel_size)
    usefull.row_left_squares(t, 1, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 2, pixel_size)
    t.right(90)
    t.forward(pixel_size)
    usefull.row_left_squares(t, 2, pixel_size)
    t.right(90)
    usefull.row_right_squares(t, 1, 2*pixel_size)
    t.backward(2*pixel_size)
    t.left(90)
    for i in range(2):
        usefull.row_left_squares(t, 1, 2*pixel_size)
        if i != 1:
            t.backward(pixel_size)
    t.up()
    t.left(90)
    t.forward(3*pixel_size)
    t.left(90)
    t.down()
    for i in range(2):
        usefull.row_right_squares(t, 1, 2*pixel_size)
        if i != 1:
            t.backward(pixel_size)
            
### TEMPORAIRE ###
from turtle import *
def play() :
    tracer(9)
    ### INITIALISATION DU GRAPHIQUE DU JEU ###
    turtle.Screen().setup(1.0, 1.0) # On force la page de jeu à avoir la plus grande taille possible
    turtle.bgcolor("#6092F5") # Fond de la page turtle bleu
    turtle.Screen().setworldcoordinates(-1280, -800, 1280, 800) # On redéfinit les coins inférieur gauche et supérieur droit
    landscape_turtle = turtle.Turtle() # On créé la tortue responsable du graphisme
    #landscape_turtle.hideturtle() # On cache cette tortue

    # Positionnement du sol
    ground_pixel_size = 6
    '''
    for line in range(2): # Deux lignes de sol pour l'effet de profondeur
        for i in range(20):
            landscape_turtle.up()
            if line == 0:
                landscape_turtle.goto(-1350, -655)
            else :
                landscape_turtle.goto(-1350, -795)
            if i != 0:
                landscape_turtle.right(90)
            landscape_turtle.forward(ground_pixel_size*23*i)
            landscape_turtle.down()
            sol(landscape_turtle, ground_pixel_size)
        landscape_turtle.setheading(0)
    '''

    # Positionnement des escaliers
    for nbMarches in range(3, 8):
        if nbMarches != 7:
            numberStairs = nbMarches
        else:
            numberStairs = nbMarches -1
        for blocNum in range(numberStairs):
            landscape_turtle.up()
            landscape_turtle.goto(-1350, -521)
            landscape_turtle.setheading(0)
            landscape_turtle.forward(ground_pixel_size*23*(nbMarches-3))
            landscape_turtle.left(90)
            landscape_turtle.forward(ground_pixel_size*23*blocNum)
            landscape_turtle.right(90)
            landscape_turtle.down()
            escaliers(landscape_turtle, ground_pixel_size)

    # Positionnement des collines

    landscape_turtle.up()
    landscape_turtle.goto(0, -521)
    landscape_turtle.down()
    landscape_turtle.setheading(0)
    colline(landscape_turtle, ground_pixel_size)

    landscape_turtle.up()
    landscape_turtle.goto(950, -521)
    landscape_turtle.down()
    landscape_turtle.setheading(0)
    colline(landscape_turtle, ground_pixel_size)

    # Positionnement du drapeau

    landscape_turtle.up()
    landscape_turtle.goto(700, -521)
    landscape_turtle.down()
    landscape_turtle.setheading(0)
    escaliers(landscape_turtle, ground_pixel_size)
    landscape_turtle.right(90)
    landscape_turtle.forward(ground_pixel_size)
    landscape_turtle.right(90)
    landscape_turtle.forward(10*ground_pixel_size)
    drapeau(landscape_turtle, 4)

    # Positionnement du buisson

    landscape_turtle.up()
    landscape_turtle.goto(911, -521)
    landscape_turtle.setheading(0)
    landscape_turtle.down()
    buisson(landscape_turtle, 2*ground_pixel_size)

    # Initialisation du plateau de jeu
    landscape_turtle.up()
    landscape_turtle.goto(-570, 600)
    landscape_turtle.setheading(0)
    landscape_turtle.down()
    landscape_turtle.color("black")
    landscape_turtle.begin_fill()
    for _ in range(2):
        landscape_turtle.forward(1100)
        landscape_turtle.circle(-50, 90)
        landscape_turtle.forward(900)
        landscape_turtle.circle(-50, 90)
    landscape_turtle.end_fill()

    landscape_turtle.up()
    landscape_turtle.right(90)
    landscape_turtle.forward(50)
    landscape_turtle.left(90)
    landscape_turtle.forward(50)
    landscape_turtle.color("#BC410D")
    landscape_turtle.down()
    landscape_turtle.begin_fill()
    for _ in range(2):
        landscape_turtle.forward(1000)
        landscape_turtle.circle(-50, 90)
        landscape_turtle.forward(800)
        landscape_turtle.circle(-50, 90)
    landscape_turtle.end_fill()
    landscape_turtle.up()


    time.sleep(5)

    # Demande de la difficulté de jeu
    input_turtle = turtle.Turtle()
    difficulty = ["facile", "normale", "difficile"]
    chosen_difficulty = "facile" #input_turtle.textinput("Choisissez la difficulté", "Sélectionnez une option : " + ", ".join(difficulty))

    # initialisation des éléments du jeu
    full_tab_elements = ["champignon", "champignon", "boo", "boo", "fleur", "fleur", "marioLuigi", "marioLuigi", 
                         "oeuf", "oeuf", "omb", "omb", "nuage", "nuage", "carapace", "carapace", 
                         "cheep", "cheep", "billBalle", "billBalle", "etoile", "etoile", "goomba", "goomba", 
                         "piece", "piece", "pow", "pow", "tanuki", "tanuki"]
    
    tab_elements = [] # tableau des éléments rempli selon la difficulté choisie

    if chosen_difficulty == "facile" :
        tab_elements = full_tab_elements[:10]
    elif chosen_difficulty == "normale" :
        tab_elements = full_tab_elements[:20]
    else :
        tab_elements = full_tab_elements

    random.shuffle(tab_elements) # on mélange le tableau

    color_tab = [] # tableau des couleurs

    for i in range(len(tab_elements)) :
        if tab_elements[i] in tab_elements[:i] : # si l'élément i est déjà passé, on insère un 2
            color_tab.append(2)
        else : # sinon, on insère un 1
            color_tab.append(1)

    turtle_tab = [] # tableau des tortues des cartes du tableau
    


    # Dessin des éléments et des cartes

    # Boucle de jeu

play()