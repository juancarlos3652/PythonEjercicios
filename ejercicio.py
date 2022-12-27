import random
def desordena(lista,tamLista,contador):
    if contador<tamLista:
        numeroRandom=random.randint(contador,tamLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordena(lista,tamLista, contador+1)
listaA=[1,2,3,4,5,6,7,8,9,10]
desordena(listaA,len(listaA),0)
print(listaA)





