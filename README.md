# Memory

>Le but de ce projet est d'écrire un jeu de memory avec comme interface graphique le module Turtle du langage Python.

## Règles du jeu

C'est un jeu en solitaire. Des cases numérotées sont réparties dans un décor, dans ces cases se cachent des objets. Quand on sélectionne 2 cases cachant le même objet, les 2 cases sont découvertes. Quand toutes les cases sont découvertes, le jeu est fini.

## Contraintes à respecter

Les objets sont des dessins faits avec Turtle, une paire contient 2 objets identiques mais de couleurs différentes. Ces objets sont situés dans un décor.

## Boucle de jeu

Le programme principal suivra l'algorithme suivant:

```
Afficher le décor
Créer un nombre pair de cases couvertes

Tant que toutes les paires ne sont pas découvertes:
    Demander un couple de n° de cases
    Découvrir les 2 cases
    Si les 2 cases contiennent le même objets, alors elles restent découvertes
    Sinon, recouvrir les 2 cases.
```