def hanoi(n):
    cpt = 0
    return 'il faut un minimum de '+str(deplace('a','b','c',n, cpt))+' deplacement pour une tour de '+str(n)+' disques'

def deplace(a, b, c, n, cpt):
    if n > 0:
        cpt += 1
        cpt = deplace(a, c, b, n-1, cpt)
        print("Move disk 1 from source",a,"to destination",c)
        cpt = deplace(b, a, c, n-1, cpt)
    return cpt
        

print(hanoi(20))