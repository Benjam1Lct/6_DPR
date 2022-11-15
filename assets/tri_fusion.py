import sys
sys.setrecursionlimit(5000)

def Fusion(T1,T2):
    if T1 == [] : return T2
    if T2 == [] : return T1
    if T1[0] < T2[0]:
        return [T1[0]] + Fusion(T1[1:],T2)
    else:
        return [T2[0]] + Fusion(T1,T2[1:])

def TriFusion(T):
    n = len(T)
    if n <=1 : return T
    T1 = T[0:(n//2)]
    T2 = T[(n//2):]
    return Fusion(TriFusion(T1),TriFusion(T2))



