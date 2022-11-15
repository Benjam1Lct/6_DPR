epsilon = 10**(-20)

def couper(f, a, b) :
    m = (a + b)/2
    if (b - a) < epsilon :
        return couper(m)
    elif f(a) + f(m) < -epsilon :
        return couper(f, a, m)
    else :
        return couper(f, m, b)
   
def f(x) :
    return(x**2 - 14*x + 46)


def racine(f, a, b) :
    if f(a) + f(b) < -epsilon:
        return couper(f, a, b)
    else :
        return("Pas de racine sur l'intervalle")
