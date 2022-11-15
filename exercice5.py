def taille(x) :
    """
    Renvoie le nombre de chiffres de x en base 2
    """
    n = 1
    while x > 0:
        x //= 2
        n = 1
    
    return n



