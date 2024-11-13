import random
import time
import turtle

from elements.dessins.billBalle import bill_balle
from elements.dessins.boo import boo
from elements.dessins.carapace import carapace
from elements.dessins.champignon import champignon
from elements.dessins.cheep import cheep
from elements.dessins.etoile import etoile
from elements.dessins.fleur import fleur
from elements.dessins.goomba import goomba
from elements.dessins.marioLuigi import mario_luigi
from elements.dessins.nuage import nuage
from elements.dessins.oeuf import oeuf
from elements.dessins.omb import omb
from elements.dessins.piece import piece
from elements.dessins.pow import pow
from elements.dessins.tanuki import tanuki
from elements.plateau.bloc import bloc
from elements.plateau.buisson import buisson
from elements.plateau.colline import colline
from elements.plateau.drapeau import drapeau
from elements.plateau.escaliers import escaliers
from elements.plateau.sol import sol


def initiate_sound():
    ### CHARGEMENT DES DIFFERENTES MUSIQUES ###
    pygame.mixer.init()
    game_music = pygame.mixer.Sound("assets/mario3ost.mp3")
    game_music.set_volume(0.3)
    game_music.play(-1)


def display_sound_effect(element):
    sound = pygame.mixer.Sound("assets/marioHitSoundEffect.mp3")
    sound.set_volume(0.8)
    match element:
        case "block":
            sound = pygame.mixer.Sound("assets/blockSoundEffect.mp3")
        case "champignon":
            sound = pygame.mixer.Sound("assets/pluslifeSoundEffect.mp3")
        case "boo":
            sound = pygame.mixer.Sound("assets/booSoundEffect.mp3")
        case "fleur":
            sound = pygame.mixer.Sound("assets/powerupSoundEffect.mp3")
        case "marioLuigi":
            sound = pygame.mixer.Sound("assets/luigiSoundEffect.mp3")
        case "oeuf":
            sound = pygame.mixer.Sound("assets/yoshiSoundEffect.mp3")
        case "omb":
            sound = pygame.mixer.Sound("assets/ombSoundEffect.mp3")
        case "nuage":
            sound = pygame.mixer.Sound("assets/lakituSoundEffect.mp3")
        case "carapace":
            sound = pygame.mixer.Sound("assets/shellSoundEffect.mp3")
        case "cheep":
            sound = pygame.mixer.Sound("assets/waterSoundEffect.mp3")
        case "billBalle":
            sound = pygame.mixer.Sound("assets/bulletBillSoundEffect.mp3")
        case "etoile":
            sound = pygame.mixer.Sound("assets/starSoundEffect.mp3")
        case "goomba":
            sound = pygame.mixer.Sound("assets/goombaSoundEffect.mp3")
        case "piece":
            sound = pygame.mixer.Sound("assets/coinSoundEffect.mp3")
        case "pow":
            sound = pygame.mixer.Sound("assets/powSoundEffect.mp3")
        case "tanuki":
            sound = pygame.mixer.Sound("assets/tanukiSoundEffect.mp3")
    sound.play()


def draw(drawing, color, t, pixel_size):
    turtle.tracer(0, 0)
    match drawing:
        case "champignon":
            champignon(t, color, pixel_size)
            return
        case "boo":
            boo(t, color, pixel_size)
            return
        case "fleur":
            fleur(t, color, pixel_size - 1)
            return
        case "marioLuigi":
            mario_luigi(t, color, pixel_size)
            return
        case "oeuf":
            oeuf(t, color, pixel_size)
            return
        case "omb":
            omb(t, color, pixel_size)
            return
        case "nuage":
            nuage(t, color, pixel_size)
            return
        case "carapace":
            carapace(t, color, pixel_size - 1)
            return
        case "cheep":
            cheep(t, color, pixel_size - 1)
            return
        case "billBalle":
            bill_balle(t, color, pixel_size)
            return
        case "etoile":
            etoile(t, color, pixel_size)
            return
        case "goomba":
            goomba(t, color, pixel_size)
            return
        case "piece":
            piece(t, color, pixel_size)
            return
        case "pow":
            pow(t, color, pixel_size - 1)
            return
        case "tanuki":
            tanuki(t, color, pixel_size)
            return
        case _:
            return


from turtle import *

import pygame


def play():
    initiate_sound()

    ### INITIALISATION DU GRAPHIQUE DU JEU ###
    turtle.Screen().setup(
        1.0, 1.0
    )  # On force la page de jeu à avoir la plus grande taille possible
    turtle.bgcolor("#6092F5")  # Fond de la page turtle bleu
    turtle.Screen().setworldcoordinates(
        -1280, -800, 1280, 800
    )  # On redéfinit les coins inférieur gauche et supérieur droit
    landscape_turtle = turtle.Turtle()  # On créé la tortue responsable du graphisme
    landscape_turtle.hideturtle()  # On cache cette tortue

    # Positionnement du sol
    turtle.tracer(0, 0)
    ground_pixel_size = 6
    for line in range(2):  # Deux lignes de sol pour l'effet de profondeur
        for i in range(20):
            landscape_turtle.up()
            if line == 0:
                landscape_turtle.goto(-1350, -655)
            else:
                landscape_turtle.goto(-1350, -795)
            if i != 0:
                landscape_turtle.right(90)
            landscape_turtle.forward(ground_pixel_size * 23 * i)
            landscape_turtle.down()
            sol(landscape_turtle, ground_pixel_size)
        landscape_turtle.setheading(0)
    turtle.update()
    turtle.tracer(9)

    # Positionnement des escaliers
    for nbMarches in range(3, 8):
        if nbMarches != 7:
            numberStairs = nbMarches
        else:
            numberStairs = nbMarches - 1
        for blocNum in range(numberStairs):
            landscape_turtle.up()
            landscape_turtle.goto(-1350, -521)
            landscape_turtle.setheading(0)
            landscape_turtle.forward(ground_pixel_size * 23 * (nbMarches - 3))
            landscape_turtle.left(90)
            landscape_turtle.forward(ground_pixel_size * 23 * blocNum)
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
    landscape_turtle.forward(10 * ground_pixel_size)
    drapeau(landscape_turtle, 4)

    # Positionnement du buisson
    landscape_turtle.up()
    landscape_turtle.goto(911, -521)
    landscape_turtle.setheading(0)
    landscape_turtle.down()
    buisson(landscape_turtle, 2 * ground_pixel_size)

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

    ### MISE EN PLACE DU JEU ###

    # Demande à l'utilisateur d'entrer la difficulté
    chosen_difficulty = turtle.textinput(
        "Choisissez une difficulté",
        "Difficultés possibles : facile(F), normale(N), difficile(D)",
    )

    # initialisation des éléments du jeu
    full_tab_elements = [
        "champignon",
        "champignon",
        "boo",
        "boo",
        "fleur",
        "fleur",
        "marioLuigi",
        "marioLuigi",
        "oeuf",
        "oeuf",
        "omb",
        "omb",
        "nuage",
        "nuage",
        "carapace",
        "carapace",
        "cheep",
        "cheep",
        "billBalle",
        "billBalle",
        "etoile",
        "etoile",
        "goomba",
        "goomba",
        "piece",
        "piece",
        "pow",
        "pow",
        "tanuki",
        "tanuki",
    ]

    tab_elements = []  # tableau des éléments rempli selon la difficulté choisie
    turtle_tab = []  # tableau des tortues des cartes du tableau
    discovered_tab = []  # tableau pour connaitre les éléments découvert

    if (
        chosen_difficulty == "facile"
        or chosen_difficulty == "F"
        or chosen_difficulty == "f"
    ):
        tab_elements = full_tab_elements[:10]
        for i in range(10):
            discovered_tab.append(False)
            toAdd = []
            t = turtle.Turtle()
            t.hideturtle()
            toAdd.append(t)
            if i < 5:
                toAdd.append(-520 + 230 * i)
                toAdd.append(380)
            else:
                toAdd.append(-520 + 230 * (i - 5))
                toAdd.append(-20)
            turtle_tab.append(toAdd)
    elif (
        chosen_difficulty == "normale"
        or chosen_difficulty == "N"
        or chosen_difficulty == "n"
    ):
        tab_elements = full_tab_elements[:20]
        for i in range(20):
            discovered_tab.append(False)
            toAdd = []
            t = turtle.Turtle()
            t.hideturtle()
            toAdd.append(t)
            if i < 5:
                toAdd.append(-520 + 230 * i)
                toAdd.append(430)
            elif i < 10:
                toAdd.append(-520 + 230 * (i - 5))
                toAdd.append(230)
            elif i < 15:
                toAdd.append(-520 + 230 * (i - 10))
                toAdd.append(30)
            else:
                toAdd.append(-520 + 230 * (i - 15))
                toAdd.append(-170)
            turtle_tab.append(toAdd)
    else:
        tab_elements = full_tab_elements
        for i in range(30):
            discovered_tab.append(False)
            toAdd = []
            t = turtle.Turtle()
            t.hideturtle()
            toAdd.append(t)
            if i < 5:
                toAdd.append(-520 + 230 * i)
                toAdd.append(480)
            elif i < 10:
                toAdd.append(-520 + 230 * (i - 5))
                toAdd.append(350)
            elif i < 15:
                toAdd.append(-520 + 230 * (i - 10))
                toAdd.append(220)
            elif i < 20:
                toAdd.append(-520 + 230 * (i - 15))
                toAdd.append(90)
            elif i < 25:
                toAdd.append(-520 + 230 * (i - 20))
                toAdd.append(-40)
            else:
                toAdd.append(-520 + 230 * (i - 25))
                toAdd.append(-170)
            turtle_tab.append(toAdd)

    random.shuffle(tab_elements)  # on mélange le tableau

    color_tab = []  # tableau des couleurs

    for i in range(len(tab_elements)):
        if (
            tab_elements[i] in tab_elements[:i]
        ):  # si l'élément i est déjà passé, on insère un 2
            color_tab.append(2)
        else:  # sinon, on insère un 1
            color_tab.append(1)

    # Dessin des éléments et des cartes
    drawing_pixel_size = 5
    drawing_turtle = (
        turtle.Turtle()
    )  # Tortue qui va dessiner une unique fois les éléments
    drawing_turtle.hideturtle()

    if (
        chosen_difficulty == "facile"
        or chosen_difficulty == "F"
        or chosen_difficulty == "f"
    ):
        for i in range(len(turtle_tab)):
            turtle_tab[i][0].up()
            if i < 5:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * i, 300)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            else:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 5), -100)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
    elif (
        chosen_difficulty == "normale"
        or chosen_difficulty == "N"
        or chosen_difficulty == "n"
    ):
        for i in range(len(turtle_tab)):
            turtle_tab[i][0].up()
            if i < 5:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * i, 350)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 10:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 5), 150)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 15:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 10), -50)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            else:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 15), -250)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()

    else:
        for i in range(len(turtle_tab)):
            turtle_tab[i][0].up()
            if i < 5:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * i, 400)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 10:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 5), 270)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 15:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 10), 140)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 20:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 15), 10)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            elif i < 25:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 20), -120)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()
            else:
                drawing_turtle.up()
                drawing_turtle.goto(-500 + 230 * (i - 25), -250)
                drawing_turtle.setheading(0)
                draw(tab_elements[i], color_tab[i], drawing_turtle, drawing_pixel_size)
                turtle_tab[i][0].up()
                turtle_tab[i][0].goto(turtle_tab[i][1], turtle_tab[i][2])
                turtle_tab[i][0].down()
                bloc(turtle_tab[i][0], drawing_pixel_size + 2)
                turtle.update()
                turtle_tab[i][0].hideturtle()

    landscape_turtle.goto(10000, 10000)

    ### BOUCLE DE JEU ###
    gameFinished = False
    while not (gameFinished):
        firstInput = -1
        secondInput = -1
        legalFirstInput = False
        legalSecondInput = False
        # Tant que les deux valeurs demandées ne sont pas bonnes on les redemande
        while not (legalFirstInput):
            # On réinitialise les valeurs
            firstInput = -1
            secondInput = -1
            legalFirstInput = False
            legalSecondInput = False

            to_discover = []
            for i in range(len(discovered_tab)):
                if not discovered_tab[i]:
                    to_discover.append(i + 1)
            string = ""
            for i in range(len(to_discover) - 1):
                string += str(to_discover[i]) + ", "
            string += str(to_discover[len(to_discover) - 1])
            firstInput = int(
                turtle.textinput(
                    "Choisissez une carte à retourner : ",
                    ("valeurs possibles : " + string),
                )
            )
            if (
                firstInput > 0
                and firstInput <= len(tab_elements)
                and not discovered_tab[firstInput - 1]
            ):
                legalFirstInput = True
                while not (legalSecondInput):
                    to_discover = []
                    for i in range(len(discovered_tab)):
                        if not discovered_tab[i] and firstInput != i + 1:
                            to_discover.append(i + 1)
                    string = ""
                    for i in range(len(to_discover) - 1):
                        string += str(to_discover[i]) + ", "
                    string += str(to_discover[len(to_discover) - 1])
                    secondInput = int(
                        turtle.textinput(
                            "Choisissez une carte à retourner : ",
                            ("valeurs possibles : " + string),
                        )
                    )
                    if (
                        secondInput > 0
                        and secondInput <= len(tab_elements)
                        and not discovered_tab[secondInput - 1]
                        and secondInput != firstInput
                    ):
                        legalSecondInput = True

        # On efface les deux cases demandées et on laisse du temps
        display_sound_effect("block")
        time.sleep(1)
        turtle_tab[firstInput - 1][0].reset()
        turtle_tab[secondInput - 1][0].reset()
        turtle.update()

        # On vérifie que les éléments découverts soient les mêmes
        if tab_elements[firstInput - 1] == tab_elements[secondInput - 1]:
            display_sound_effect(tab_elements[firstInput - 1])
            discovered_tab[firstInput - 1] = True
            discovered_tab[secondInput - 1] = True
            # On vérifie qu'on soit à la fin du jeu
            hasFalse = False
            for i in range(len(discovered_tab)):
                if not (discovered_tab[i]):
                    hasFalse = True
                    break
            if not (hasFalse):
                gameFinished = True
        else:
            # Son mauvaise réponse
            display_sound_effect("wrong")
            time.sleep(2)
            # On remet les cases effacées
            turtle_tab[firstInput - 1][0].up()
            turtle_tab[firstInput - 1][0].goto(
                turtle_tab[firstInput - 1][1], turtle_tab[firstInput - 1][2]
            )
            turtle_tab[firstInput - 1][0].down()
            bloc(turtle_tab[firstInput - 1][0], drawing_pixel_size + 2)
            turtle_tab[firstInput - 1][0].hideturtle()

            turtle_tab[secondInput - 1][0].up()
            turtle_tab[secondInput - 1][0].goto(
                turtle_tab[secondInput - 1][1], turtle_tab[secondInput - 1][2]
            )
            turtle_tab[secondInput - 1][0].down()
            bloc(turtle_tab[secondInput - 1][0], drawing_pixel_size + 2)
            turtle_tab[secondInput - 1][0].hideturtle()

    time.sleep(3)
