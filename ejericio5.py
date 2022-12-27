import time
def fibonacciIterativa(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return b
print(fibonacciIterativa(4))
def fibonacciRecursiva(n):
    if n <2:
        resultado=1
    else:
        resultado= fibonacciIterativa(n-1)+fibonacciRecursiva(n-2)
    return resultado
for x in range(6):
    print(fibonacciRecursiva(x))
t0=time.time()
a= fibonacciRecursiva(4)
t1=time.time()
print(a,t1-t0)
t3=time.time()
b= fibonacciIterativa(4)
t4=time.time()
print(b,t4-t3)







    