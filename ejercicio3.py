def ordenarLista(lista,tamLista,contador):
    if contador<tamLista:
        pequeño=lista[contador]
        posicion=contador
        for i in range(contador+1,tamLista):
            if lista[i]<pequeño:
                pequeño=lista[i]
                posicion=i
        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        ordenarLista(lista,tamLista,contador+1)
listaA=[6,9,3,4,2,1,7,5,8,10]
ordenarLista(listaA,len(listaA),0)
print(listaA)

    
     

    

