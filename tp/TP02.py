import time


# exercice 1.1
def diviseurs(n):
    list_diviseurs = []
    for i in range(1, n+1):
        if n%i == 0:
            list_diviseurs += [i]
    return list_diviseurs

print(diviseurs(28))


# exercice 2.1
def pgcd_naif(a, b):
    diviseur = 1
    for i in range(1, min(a,b) +1):
        if a%i == 0 and b%i == 0:
            diviseur = i
    return diviseur


def pgcd(a, b):
    while b!= 0:
        a, b = b,a%b
    return a 


print(pgcd_naif(1071, 462), pgcd(1071, 462))


# exercice 3.1
def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter()-debut



def est_premier_naif(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def est_premier(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


print(est_premier_naif(97), est_premier_naif(91))
for i in (10_007, 100_003, 1_000_003):
    t_naif = duree(est_premier_naif, i)
    t_rac = duree(est_premier, i)
    print(f"{i:>9} : naif {t_naif:.5f} s | racine {t_rac:.6f} s")


# exercice 4.1
def est_premier(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True



def crible(limite):
    est_premier_tab = [True] * (limite + 1)
    est_premier_tab[0] = False
    if limite >= 1:
        est_premier_tab[1] = False
    d = 2
    while d * d <= limite:
        if est_premier_tab[d]:
            for multiple in range(d * d, limite + 1, d):
                est_premier_tab[multiple] = False
        d = d + 1
    return [n for n in range(limite + 1) if est_premier_tab[n]]


debut = time.perf_counter()
p = crible(100000)
t_crible = time.perf_counter() - debut


debut = time.perf_counter()
combien = sum(1 for i in range(100001) if est_premier(i))
t_un = time.perf_counter() - debut

print(len(p), combien)
print(f"crible {t_crible:.4f} s | un par un {t_un:.4f} s")


# exercice 5.1

def facteurs(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
print(f)

produit = 1
for x in f:
    produit = produit * x
print(produit)

# exercice 6.1

def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter()-debut


def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print([fibonacci_recursif(n) for n in range(15)])


for n in (20, 25, 30):
    print(f"F({n}) : {duree(fibonacci_recursif, n):.4f} s")



# exercice 6.2
d = {}

def fibonacci_compte(n):
    d[n] = d.get(n, 0) + 1
    if n < 2:
        return n
    return fibonacci_compte(n - 1) + fibonacci_compte(n - 2)

res = fibonacci_compte(30)
print("F(30) =", res)
print("appels a F(1) :", d[1])
print("appels en tout :", sum(d.values()))


# exercice 6.3


def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    return time.perf_counter()-debut


def fibonacci_recursif(n):
    if n < 2:
        return n
    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print([fibonacci_recursif(n) for n in range(15)])


def fibonacci(n):
    n_1, n_2 = 0, 1
    for _ in range(n):
        n_1, n_2 = n_2, n_1 + n_2
    return n_1

print(all(fibonacci(n) == fibonacci_recursif(n) for n in range(26)))
print(f"F(30) en {duree(fibonacci, 30):.6f} s")
grand = fibonacci(10_000)
print(len(str(grand)), "chiffres")


# exercice 7.1

def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0
    g, u, v = euclide_etendu(b, a % b)
    return g, v, u - (a // b) * v

g, u, v = euclide_etendu(1071, 462)
print(g, u, v, 1071 * u + 462 * v == g)



# exercice 7.2


def puissance_mod_naive(a, e, n):
    resultat = 1
    for i in range(e):
        resultat = resultat * a % n
    return resultat

def puissance_mod(a, e, n):
    resultat = 1
    a = a % n
    while e > 0:
        if e % 2 == 1:
            resultat = resultat * a % n
        a = a * a % n
        e = e // 2
    return resultat

a, e, n = 7, 10 ** 7, 1_000_003
print(puissance_mod(a, e, n), pow(a, e, n))

debut = time.perf_counter()
puissance_mod_naive(a, e, n)
t_naive = time.perf_counter() - debut
debut = time.perf_counter()
puissance_mod(a, e, n)
t_rapide = time.perf_counter() - debut
print(f"naive {t_naive:.3f} s | rapide {t_rapide:.6f} s")





