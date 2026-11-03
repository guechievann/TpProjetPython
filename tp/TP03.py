import time
import math


# exercice 1.1
def evaluer_naif(P, x):
    res = 0
    for i in range(len(P)):
        res += P[i] * x **i
    return res

print(evaluer_naif([2,3,0,5], 2))



# exercice 2.1
def evaluer_naif(P, x):
    res = 0
    for i in range(len(P)):
        res += P[i] * x **i
    return res




def evaluer(P, x):
    res = 0
    for i in reversed(P):
        res = res * x +i
    return res

P = [2,3,0,5]
for i in (-2,0,1,2,10):
    print(i, evaluer_naif(P,i), evaluer(P, i))



# exercice 2.2


def evaluer_naif(P, x):
    res = 0
    for i in range(len(P)):
        res += P[i] * x **i
    return res




def evaluer(P, x):
    res = 0
    for i in reversed(P):
        res = res * x +i
    return res



for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 1.0001)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>6} : naif {t_naif:.5f} s | horner {t_horner:.5f} s "
          f"| rapport {t_naif / t_horner:.1f} | ecart des valeurs {abs(a - b):.2e}")



#exercice 2.3

for degre in (200, 400, 800):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 3)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>6} : naif {t_naif:.5f} s | horner {t_horner:.5f} s "
          f"| rapport {t_naif / t_horner:.1f} | ecart des valeurs {abs(a - b):.2e}")



# exercice 3.1
def deriver(P):
    res = []
    for i in range(1, len(P)):
        res += [i*P[i]]
    return res


print(deriver([2, 3, 0, 5]))


# exercice 4.1
def dichotomie(f, a, b, tolerance):
    fa = f(a)
    fb= f(b)
    if fa == 0:
        return a
    elif fb == 0:
        return b
    elif fa* fb>0:
        print("error")
    while b-a > tolerance:
        milieu = (a+b)/2
        if f(a) * f(milieu)<=0:
            b = milieu
        else:
            a = milieu
    return (a+b)/2

def carre_moins_deux(x):
    return x * x -2

racine = dichotomie(carre_moins_deux, 0 , 2, 1e-12 )
print(racine)



# exercice 4.2
def newton(P, depart, tolerance=1e-12, tours_max=100):
    d = deriver(P)
    x = float(depart)
    for i in range(tours_max):
        valeur = evaluer(P, x)
        pente = evaluer(d, x)
        if pente == 0:
            print ("error")
        suivant = x - valeur / pente
        if abs(suivant - x) <= tolerance * max(1.0, abs(suivant)):
            return suivant, i + 1
        x = suivant

Q = [-5, -2, 0, 1]
racine, tours = newton(Q, 2)
print(racine, "en", tours, "tours")


# exercice 4.3

def newton2(P, depart, tours):
    d = deriver(P)
    x = float(depart)
    trajet = [x]
    for i in range(tours):
        pente = evaluer(d, x)
        if pente == 0:
            break
        x = x - evaluer(P, x) / pente
        trajet.append(x)
    return trajet
R = [2, -2, 0, 1] 
print(newton2(R, 0, 8))

# exercice 4.4
Q = [-5, -2, 0, 1]
for depart in (2,1,0):
    racine, tours = newton(Q, depart)
    print(f"depart {depart:>2} : {tours:>2} tours, racine {racine:.9f}")


# exercice 5.1
print("La courbe coupe une seule fois l'axe des abscisses, c'est donc la seule solution réelle")


# exercice 6.1
def somme(P,Q):
    longueur = max(len(P), len(Q))
    P = P + [0] * (longueur - len(P))
    Q = Q + [0] * (longueur - len(Q))
    for i in range(longueur):
        return [P[i] + Q[i]]




def produit_poly(P,Q):
    if not P or not Q:
        return []
    R = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] = R[i + j] + P[i] * Q[j]
    return R

print(somme([1, 2], [0, 0, 3]))
print(produit_poly([1, 1], [1, 1]))
print(produit_poly([-1, 1], [1, 1]))


# exercice 6.2
def produit_poly(P,Q):
    if not P or not Q:
        return []
    R = [0] * (len(P) + len(Q) - 1)
    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] = R[i + j] + P[i] * Q[j]
    return R

binome = [1]
for _ in range(10):
    binome = produit_poly(binome, [1, 1])
print(binome)


# exercice 7.1


def derivee_avant(f, x, h):
    return (f(x + h) - f(x)) / h

def derivee_centree(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

exacte = math.cos(1.0)
for h in (1e-1, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12):
    e_avant = abs(derivee_avant(math.sin, 1.0, h) - exacte)
    e_centree = abs(derivee_centree(math.sin, 1.0, h) - exacte)
    print(f"h = {h:.0e} : avant {e_avant:.1e} | centree {e_centree:.1e}")





# exercice 8.1


def rectangles(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))

def trapezes(f, a, b, n):
    h = (b - a) / n
    interieur = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + interieur)

def simpson(f, a, b, n):
    if n % 2 == 1:
        n = n + 1
    h = (b - a) / n
    impairs = sum(f(a + i * h) for i in range(1, n, 2))
    pairs = sum(f(a + i * h) for i in range(2, n, 2))
    return h / 3 * (f(a) + f(b) + 4 * impairs + 2 * pairs)

def carre(x):
    return x * x

for n in (10, 100, 1000):
    e_rect = abs(rectangles(carre, 0, 1, n) - 1 / 3)
    e_trap = abs(trapezes(carre, 0, 1, n) - 1 / 3)
    e_simp = abs(simpson(carre, 0, 1, n) - 1 / 3)
    print(f"n = {n:>4} : rectangles {e_rect:.1e} | trapezes {e_trap:.1e} | simpson {e_simp:.1e}")


# exercice 8.2
def arctangente_derivee(x):
    return 4 / (1 + x * x)

trap = trapezes(arctangente_derivee, 0, 1, 1000)
simp = simpson(arctangente_derivee, 0, 1, 1000)
print(trap, abs(trap - math.pi))
print(simp, abs(simp - math.pi))


