def ordenamientoInsercion(lista):
    n=len(lista)
    for i in range(1,n):
        for j in range(i,0,-1):
            if lista[j]<lista[j-1]:
                aux=lista[j-1]
                lista[j-1]=lista[j]
                lista[j]=aux

def __main__():
    lista=[3,7,8,2]
    ordenamientoInsercion(lista)
    print(lista)
if __name__=="__main__":
    __main__()