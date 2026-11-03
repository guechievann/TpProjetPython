
import math
import random
import matplotlib.pyplot as plt


GRAVITE = 9.81
HAUTEUR_BUT = 2.44
RAYON_BALLON = 0.11


def evaluer_polynome(coefficients, x):
    valeur = 0.0
    for coefficient in reversed(coefficients):
        valeur = valeur * x + coefficient
    return valeur


def dichotomie(fonction, gauche, droite, tolerance=1e-10):
    valeur_gauche = fonction(gauche)
    valeur_droite = fonction(droite)

    if valeur_gauche == 0:
        return gauche
    if valeur_droite == 0:
        return droite
    if valeur_gauche * valeur_droite > 0:
        raise ValueError("L'intervalle ne contient pas de changement de signe.")

  
    while droite - gauche > tolerance:
        milieu = (gauche + droite) / 2
        valeur_milieu = fonction(milieu)

        if valeur_milieu == 0:
            return milieu
        if valeur_gauche * valeur_milieu < 0:
            droite = milieu
        else:
            gauche = milieu
            valeur_gauche = valeur_milieu
    return (gauche + droite) / 2


def newton(fonction, derivee, depart, tolerance=1e-10, tours_max=100):
    x = float(depart)
    for _ in range(tours_max):
        pente = derivee(x)
        if abs(pente) < 1e-14:
            raise ZeroDivisionError("La derivee est trop proche de zero.")
        suivant = x - fonction(x) / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant
        x = suivant
    raise RuntimeError("La methode de Newton n'a pas converge.")


def multiplier_matrices(A, B):
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Dimensions incompatibles pour le produit matriciel.")
    resultat = []
    for i in range(len(A)):
        ligne = []
        for j in range(len(B[0])):
            somme = 0
            for k in range(len(B)):
                somme = somme + A[i][k] * B[k][j]
            ligne.append(somme)
        resultat.append(ligne)
    return resultat


def transformer_point(matrice, point):
    x, y = point
    point_homogene = [x, y, 1]
    resultat = []
    for i in range(3):
        coordonnee = 0
        for j in range(3):
            coordonnee = coordonnee + matrice[i][j] * point_homogene[j]
        resultat.append(coordonnee)

    if resultat[2] == 0:
        raise ValueError("Transformation invalide : coordonnee homogene nulle.")
    return resultat[0] / resultat[2], resultat[1] / resultat[2]


def aire_polygone(sommets):
    somme = 0.0
    for i, (x1, y1) in enumerate(sommets):
        x2, y2 = sommets[(i + 1) % len(sommets)]
        somme += x1 * y2 - x2 * y1
    return abs(somme) / 2


def dedans_polygone(point, sommets):
    x, y = point
    dedans = False
    for i, (x1, y1) in enumerate(sommets):
        x2, y2 = sommets[(i + 1) % len(sommets)]
        if (y1 > y) != (y2 > y):
            x_intersection = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_intersection:
                dedans = not dedans
    return dedans


def trajectoire(vitesse, angle_degres, distance):
    angle = math.radians(angle_degres)
    vitesse_horizontale = vitesse * math.cos(angle)
    if vitesse_horizontale <= 0:
        raise ValueError("La vitesse horizontale doit etre positive.")
    a = -GRAVITE / (2 * vitesse_horizontale**2)
    b = math.tan(angle)
    c = RAYON_BALLON
    coefficients = [c, b, a]

    hauteur = lambda x: evaluer_polynome(coefficients, x)
    derivee = lambda x: b + 2 * a * x
    return coefficients, hauteur, derivee


def premier_croisement(fonction, distance, niveau, pas=0.1):
    ecart = lambda x: fonction(x) - niveau
    precedent = 0.0
    valeur_precedente = ecart(precedent)
    nombre_intervalles = max(1, math.ceil(distance / pas))
    for i in range(1, nombre_intervalles + 1):
        courant = min(i * pas, distance)
        valeur_courante = ecart(courant)
        if valeur_courante == 0:
            return courant
        if valeur_precedente * valeur_courante < 0:
            return dichotomie(ecart, precedent, courant)
        precedent = courant
        valeur_precedente = valeur_courante
    return None


def afficher_terrain(fonction, distance, mur_x, hauteur_mur):
    xs = [distance * i / 300 for i in range(301)]
    ys = [fonction(x) for x in xs]
    hauteur_max = max(HAUTEUR_BUT, hauteur_mur, max(ys)) + 0.5

    figure, axes = plt.subplots(figsize=(11, 5))
    axes.plot(xs, ys, color="royalblue", label="Trajectoire du ballon")
    axes.axhline(0, color="forestgreen", linewidth=2, label="Sol")

    axes.vlines(mur_x, 0, hauteur_mur, color="darkorange", linewidth=5, label="Mur" )
    axes.vlines(distance, 0, HAUTEUR_BUT, color="black", linewidth=3, label="Poteaux")
    axes.hlines(HAUTEUR_BUT,distance - 0.15,distance + 0.15,color="black",linewidth=3,label="Barre transversale")
    axes.scatter([mur_x, distance],[fonction(mur_x), fonction(distance)], color=["darkorange", "crimson"],zorder=3)
    axes.annotate("Ballon au mur",(mur_x, fonction(mur_x)), xytext=(6, 8),textcoords="offset points")
    axes.annotate("Ballon au but",(distance, fonction(distance)), xytext=(-85, 10), textcoords="offset points")
    axes.set(title="Simulation d'un coup franc",xlabel="Distance depuis le ballon (m)",ylabel="Hauteur (m)",xlim=(0, distance + 1),ylim=(0, hauteur_max))
    axes.grid(True, linestyle=":", alpha=0.6)
    axes.legend()
    figure.tight_layout()
    plt.show()
    but = [(distance, 0.0),(distance, HAUTEUR_BUT),(distance + 0.5, HAUTEUR_BUT),(distance + 0.5, 0.0)]
    return aire_polygone(but)


def simuler_tirs(nombre, generateur, distance, mur_x, hauteur_mur, vitesse, angle):
    reussites = 0
    for _ in range(nombre):
        vitesse_tir = vitesse + generateur.uniform(-1.0, 1.0)
        angle_tir = angle + generateur.uniform(-0.5, 0.5)
        _, hauteur, _ = trajectoire(vitesse_tir, angle_tir, distance)
        if hauteur(mur_x) >= hauteur_mur + RAYON_BALLON:
            if RAYON_BALLON <= hauteur(distance) <= HAUTEUR_BUT - RAYON_BALLON:
                reussites += 1

    return reussites, nombre


def main():
    print("Le modele est en 2D et ne tient pas compte des frottements ni de l'effet.")
    generateur = random.Random()
    distance = generateur.uniform(16.0, 25.0)
    mur_x = generateur.uniform(0.4 * distance, 0.6 * distance)
    hauteur_mur = generateur.uniform(1.4, 2.0)
    vitesse = generateur.uniform(25.0, 32.0)
    angle = generateur.uniform(10.0, 18.0)

    print("\nParametres tires au hasard avec la bibliotheque random :")
    print(f"Distance du ballon au but : {distance:.1f} m")
    print(f"Distance du mur au ballon : {mur_x:.1f} m")
    print(f"Hauteur du mur : {hauteur_mur:.2f} m")
    print(f"Vitesse initiale : {vitesse:.1f} m/s")
    print(f"Angle de tir : {angle:.1f} degres")

    coefficients, hauteur, derivee = trajectoire(vitesse, angle, distance)
    hauteur_mur_ballon = hauteur(mur_x)
    hauteur_but = hauteur(distance)
    franchit_mur = hauteur_mur_ballon >= hauteur_mur + RAYON_BALLON

    print("\nPolynome de trajectoire :")
    print(f"y(x) = {coefficients[0]:.6f} + "f"{coefficients[1]:.6f} x + ({coefficients[2]:.6f}) x^2")
    print(f"Hauteur au niveau du mur : {hauteur_mur_ballon:.2f} m")
    print(f"Hauteur au niveau du but : {hauteur_but:.2f} m")

    croisement_mur = premier_croisement(hauteur, distance, hauteur_mur + RAYON_BALLON)
    if croisement_mur is not None:
        print("Croisement avec le haut du mur (dichotomie) : "f"x = {croisement_mur:.3f} m")
        try:
            racine_newton = newton(lambda x: hauteur(x) - hauteur_mur - RAYON_BALLON,derivee,croisement_mur)
            print(f"Meme racine par Newton : x = {racine_newton:.3f} m")
        except (RuntimeError, ZeroDivisionError):
            print("Newton n'a pas converge pour ce croisement.")

    ouverture_but = [(distance, RAYON_BALLON),(distance, HAUTEUR_BUT - RAYON_BALLON),(distance + 0.5, HAUTEUR_BUT - RAYON_BALLON),(distance + 0.5, RAYON_BALLON)]
    ballon_dans_ouverture = dedans_polygone((distance + 0.25, hauteur_but), ouverture_but)
    if not franchit_mur:
        print("\nResultat : le ballon touche le mur.")
    elif ballon_dans_ouverture:
        print("\nResultat : le ballon passe le mur et entre dans le but !")
    elif hauteur_but > HAUTEUR_BUT - RAYON_BALLON:
        print("\nResultat : le ballon passe au-dessus de la barre.")
    elif hauteur_but < RAYON_BALLON:
        print("\nResultat : le ballon passe sous le cadre.")
    else:
        print("\nResultat : le ballon sort de l'ouverture du but.")

    surface_but = afficher_terrain(hauteur, distance, mur_x, hauteur_mur)


    


if __name__ == "__main__":
    main()
