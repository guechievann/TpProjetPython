import math
import sys
import fractions

# exercice 1.1
n = 2026
d = 7
quotient = n // d
reste = n % d
print(quotient, reste)
print(quotient * d + reste == n)



# exercice 1.2
n = 123456789
print(n%10)
print(n//10)



# exercice 2.1
resultat = 0
n = 0.1
for i in range(0, 1000):
    resultat += n
print(resultat)
print(100-resultat)



# exercice 2.2  
def presque_egaux(a, b):
    return abs(a - b)
print(presque_egaux(0.1+0.2, 0.3)!=0)
print(presque_egaux(1.0, 1.5)!=0)


# exercice 3.1
n = 7
for i in range(1, 11):
    print(n, "x" , i , "=" , n*i )
    print("\n")



# exercice 3.2
resultat1 = 0
resultat2 = (100*(100+1))//2
for i in range(1, 101):
    resultat1 += i
print(resultat1)
print(resultat2)


# exercice 4.1
def nombre_de_chiffres(n):
    index = 1
    while n>=10:
        n=n//10
        index+=1
    return index
print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))




# exercice 5.1


def heron(a):
    if a < 0:
        return None
    if a == 0:
        return 0
    x=float(a)
    tolerance = 1e-12
    index = 0
    while True:
        n_1 = 0.5*(x+a/x)
        index+=1
        if abs(n_1 - x) <= tolerance * abs(n_1):
            return n_1
        x=n_1

print(abs(heron(2) - math.sqrt(2)))




# exercice 6.1
def vers_binaire(n):
    if n == 0:
        return "0"
    chaine = ""
    while n > 0:
        chaine = str(n % 2) + chaine
        n = n // 2
    return chaine

print(vers_binaire(37))
print(vers_binaire(0))




# exercice 6.2

eps = 1.0
while 1.0 + eps / 2 != 1.0:
    eps = eps /2
print(abs(eps - sys.float_info.epsilon))


# exercice 7.1

def racines_naif(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    return (-b - r) / (2 * a), (-b + r) / (2 * a)

petite, grande = racines_naif(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande, "attendu : 1")


# exercice 7.2

def racines(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        raise ValueError("pas de racine réelle")
    r = math.sqrt(delta)
    
    if b >= 0:
        sure = (-b - r) / (2 * a)
    else:
        sure = (-b + r) / (2 * a)
    autre = c / (a * sure)
    return min(sure, autre), max(sure, autre)

petite, grande = racines(1.0, -1e8, 1.0)
print(petite, grande)
print("produit :", petite * grande)
for x in (petite, grande):
    residu = x * x - 1e8 * x + 1
    print(f"residu : {residu:.1e}, soit {residu / max(x * x, 1.0):.1e} en relatif")

# exercice 7.3

total = fractions.Fraction(0)
for _ in range(1000):
    total = total + fractions.Fraction(1, 10)
print(total, total == 100)
print(fractions.Fraction(1, 10) + fractions.Fraction(2, 10) == fractions.Fraction(3, 10))