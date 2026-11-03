import unicodedata
from collections import Counter
import random



# exercice 1.1
def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    return chr(n % 26 + ord("A"))

print(lettre_vers_nombre("C"), nombre_vers_lettre(2))
print([nombre_vers_lettre(lettre_vers_nombre(c)) == c for c in "ABCXYZ"])



# exercice 1.2


def nettoyer(texte):
    sans_accent = unicodedata.normalize("NFD", texte)
    sans_accent = "".join(c for c in sans_accent if unicodedata.category(c) != "Mn")
    return "".join(c for c in sans_accent.upper() if "A" <= c <= "Z")


print(nettoyer("Été, à Paris !"))


# exercice 2.1
def chiffrer(texte, a,b):
    res = []
    for c in nettoyer(texte):
        x = lettre_vers_nombre(c)
        res.append(nombre_vers_lettre((a*x+b)%26))
    return "".join(res)


texte = "ATTAQUEALAUBE"
print(chiffrer(texte, 5, 8))
print(chiffrer(texte, 1, 3))


# exercice 3.1
def pgcd(a, b):
    while b!=0:
        a , b = b, a%b
    return a


liste = [a for a in range(1, 26) if pgcd(a, 26) == 1]
print(liste)
print(len(liste), "valeurs possibles pour a")


# exercice 3.2
def inverse_modulaire(a,n):
    a =a % n
    for i in range(1, n):
        if (a * i ) % n == 1:
            return i
    print("n'est pas inversible")


print(inverse_modulaire(5,26))
print((5*21)%26)

# exercice 4.1

def dechiffrer(texte, a, b):
    a_inverse = inverse_modulaire(a, 26)
    res = []
    for i in nettoyer(texte):
        y = lettre_vers_nombre(i)
        res.append(nombre_vers_lettre(a_inverse * (y - b) % 26))
    return "".join(res)


texte = nettoyer("Attaque a l aube")
texte_secret = chiffrer(texte, 5, 8)
print(texte_secret)
print(dechiffrer(texte_secret, 5, 8))
print(dechiffrer(texte_secret, 5, 8) == texte)



# exercice 5.1

valides = [a for a in range(1, 26) if pgcd(a, 26) == 1]

def toutes_les_clefs(texte_secret):
    resultats = []
    for a in valides:
        for b in range(26):
            resultats.append((a, b, dechiffrer(texte_secret, a, b)))
    return resultats


texte = nettoyer("Attaque a l aube")
texte_secret = chiffrer(texte, 5, 8)
essais = toutes_les_clefs(texte_secret)
print(len(essais), "clefs essayees")
bons = [e for e in essais if e[2] == texte]
print("la bonne clef :", bons[0][0], bons[0][1])



# exercice 6.1

texte_long = nettoyer(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
  
)
secret_long = chiffrer(texte_long, 7, 12)

comptes = Counter(secret_long)
lettre_frequente = comptes.most_common(1)[0][0]
print("lettre la plus frequente du chiffre :", lettre_frequente)


cible = lettre_vers_nombre(lettre_frequente)
candidats = []
for a in valides:

    b = (cible - 4 * a) % 26
    candidats.append((a, b, dechiffrer(secret_long, a, b)))

print(len(candidats), "candidats au lieu de 312")
for a, b, texte in candidats:
    if texte.startswith("LECHIFFREMENT"):
        print("trouve :", a, b)
        print(texte[:100])



# exercice 7.1

texte_long = nettoyer(
    "Le chiffrement affine est un chiffrement par substitution monoalphabetique. "
  
)
secret_long = chiffrer(texte_long, 7, 12)

def indice_coincidence(texte):
    N = len(texte)
    comptes = Counter(texte)
    return sum(n * (n - 1) for n in comptes.values()) / (N * (N - 1))

random.seed(1)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
hasard = "".join(random.choice(alphabet) for _ in range(len(texte_long)))

print(f"clair    : {indice_coincidence(texte_long):.4f}")
print(f"affine   : {indice_coincidence(secret_long):.4f}")
print(f"hasard   : {indice_coincidence(hasard):.4f}")




# exercice 8.1

def indice_coincidence(texte):
    N = len(texte)
    comptes = Counter(texte)
    return sum(n * (n - 1) for n in comptes.values()) / (N * (N - 1))

def vigenere(texte, cle):
    resultat = []
    for i, c in enumerate(nettoyer(texte)):
        decalage = lettre_vers_nombre(cle[i % len(cle)])
        resultat.append(nombre_vers_lettre(lettre_vers_nombre(c) + decalage))
    return "".join(resultat)

secret_vigenere = vigenere(texte_long, "CLE")
print(secret_vigenere[:40])
print(f"IC vigenere : {indice_coincidence(secret_vigenere):.4f}")