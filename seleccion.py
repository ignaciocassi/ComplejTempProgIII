def ordenamientoSeleccion(lista):
    n=len(lista)
    for i in range(n):
        for j in range(i+1,n):
            if lista[j]<lista[i]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux

def __main__():
    lista=[3,7,8,2]
    ordenamientoSeleccion(lista)
    print(lista)

if __name__=="__main__":
    __main__()