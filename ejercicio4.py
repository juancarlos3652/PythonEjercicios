import time 
def factorialRecursivo(n):
    if n==0:
        resultado=1
    else:
        resultado= n * factorialRecursivo(n-1)
    return resultado
print(factorialRecursivo(4))
def factoriaIterativa(n):
    resultado=1
    for i in range(n):
        resultado*= n-i
    return resultado
t0=time.time()
a=factorialRecursivo(800)
t1=time.time()
print(a,t1-t0)
t2 =time.time()
b=factoriaIterativa(800)
t3=time.time()
print(b,t3-t2)

