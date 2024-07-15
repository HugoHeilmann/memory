import turtle
import random

def play() :
    # Initialisation du graphique de jeu

    # Initialisation du plateau de jeu

    # Demande de la difficulté de jeu
    input_turtle = turtle()
    difficulty = ["facile", "normale", "difficile"]
    chosen_difficulty = input_turtle.textinput("Choisissez la difficulté", "Sélectionnez une option : " + ", ".join(difficulty))

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