# TpProjetPython


# Simulateur de coup franc

Ce programme Python simule en deux dimensions la trajectoire d'un ballon lors d'un coup franc. Il tire au hasard les paramètres du tir (distance au but, position et hauteur du mur, vitesse et angle), puis estime si le ballon franchit le mur et entre dans l'ouverture du but.

Le modèle utilise une trajectoire parabolique sous l'effet de la gravité. Il ne prend pas en compte les frottements de l'air ni l'effet du ballon. Le fichier contient également des fonctions numériques pour trouver des racines par dichotomie et par la méthode de Newton et vérifier si un point est dans un polygone.

## Prérequis

- Python 3
- Matplotlib

Installer Matplotlib si nécessaire :

```bash
python -m pip install matplotlib
```

## Lancer le programme

Dans un terminal, placez-vous dans le dossier contenant `simulateur_coup_franc.py`, puis exécutez :

```bash
python simulateur_coup_franc.py
```

Selon votre installation, la commande peut être `python3` à la place de `python`.

## Ce qu'on doit observer

À chaque exécution, les paramètres aléatoires changent. Le terminal affiche notamment :

- les paramètres du tir;
- l'équation polynomiale de la trajectoire;
- la hauteur du ballon au niveau du mur et du but;
- si un croisement avec le haut du mur est détecté, sa position calculée par dichotomie puis, si elle converge, par Newton;
- le résultat du tir : le ballon touche le mur, entre dans le but, passe au-dessus ou sous le cadre, ou sort de l'ouverture.

Une fenêtre Matplotlib s'ouvre également avec la trajectoire, le sol, le mur et le but. Les points du ballon au niveau du mur et du but y sont indiqués. Fermez la fenêtre pour terminer l'exécution.

Le résultat est donc susceptible d'être différent d'un lancement à l'autre, puisque les paramètres sont générés aléatoirement.
