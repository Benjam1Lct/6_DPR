from random import randint
import matplotlib.pyplot as plt
import numpy as np
import math

def recherche_dicho(val, tab):
    compteur = 0
    g = 0
    d = len(tab)
    while g < d - 1:
        compteur += 1
        m = (g + d)//2
        if val == tab[m]:
            return(m, compteur)
        elif val > tab[m]:
            g = m
        else:
            d = m
    return(None, compteur)

def tableau_trie(n):
    """ 
    Génère et retourne un tableau de n entiers triés dans l'ordre croissant
    """
    # On initialise un tableau contanentant n zéros
    tab = [0 for i in range (0, n)]
    # On choisit un nombre entier aléatoire entre 1 et 100
    # On l'affecte à la prmeière place du tableau
    tab[0] = randint(1, 100)
    # pour chacune des n-1 dernièrs éléments du tableau
    # on ajoute un nombre entier aléatoire entre 1 et 100
    # à la valeur précédente
    for i in range(0, n - 1):
        tab[i + 1] = tab[i] + randint(0, 100)
    return tab


#######  MAIN  ###########################

abscisses_bis = []
ordonnées_bis = []

for i in range(1, 10**5, 1000):
    somme_tours_boucles = 0
    tab = tableau_trie(i)
    for j in range (100):
        val = tab[randint(0, len(tab) - 1)]
        somme_tours_boucles = somme_tours_boucles + recherche_dicho(val, tab)[1]
    abscisses_bis.append(i)
    ordonnées_bis.append(somme_tours_boucles / 100)
	
### tracé avec mlatplotlib

abscisses = np.linspace(1, 10**5, 1000)
ordonnées = [math.log2(x) for x in abscisses]
plt.plot(abscisses,ordonnées)
plt.plot(abscisses_bis,ordonnées_bis)
plt.show()


