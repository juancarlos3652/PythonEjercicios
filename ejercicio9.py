import numpy as np

def sumarValores(n,m):
    if m==0:
        suma=n+1*m
    else:
        suma= n + sumarValores(n,m-1)
    return suma
print(sumarValores(3,4))


