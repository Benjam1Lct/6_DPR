from random import randint
import sys
sys.setrecursionlimit(5000)

def recherche(val, tab, g, d):
    """renvoie une position de val dans tab[g..d],
        supposé trié, et None si elle ne s'y trouve pas"""
    m = (g+d)//2
    if val == tab[m]:
        return m
    else:
        return recherche(val, tab, g, d)
    
def recherche_dichotomique_recursive(val, tab):
    """renvoie une position de element dans tableau,
        supposé trié, et None si elle ne s'y trouve pas"""
    return recherche(val, tab, 0, len(tab)-1)
    

def tableau_trie(n):
    """
    Génère et retourne un tableau de n entiers triés dans l'ordre croissant
    """
    # On initialise un tableau contanentant n zéros
    tab = [0 for i in range (0,n )]
    # On choisit un nombre entier aléatoire entre 1 et 100
    # On l'affecte à la prmeière place du tableau
    tab[0] = randint(1,100)
    # pour chacune des n-1 dernièrs éléments du tableau
    # on ajoute un nombre entier aléatoire entre 1 et 100
    # à la valeur précédente
    for i in range(0, n - 1):
        tab[i + 1] = tab[i] + randint(0, 100)
    return tab


t = [1,2,3,4,5,6,7,8,9,11,12,16,48,89]
print(recherche_dichotomique_recursive(11, t))