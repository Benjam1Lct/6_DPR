def taille(x, t = 0) :
    """
    Renvoie le nombre de chiffres de x en base 2
    """
    if x <= 1 :
        return t+1
    else :
        t += 1
        return taille(x//2, t)