def quickSort(S,inicio,fin):
    if inicio<fin:
        p=pivot(S,inicio,fin)
        quickSort(S,inicio,p-1)
        quickSort(S,p+1,fin)

def pivot(S,inicio,fin):
    p=S[inicio]                        #p= Valor del elemento 0
    k=inicio+1                         #k= Indice iniciado en pos 1
    l=fin                              #l= Indice iniciado la últ. pos.
    while S[k]<=p and k<fin:           #Mientras que el valor de K sea menor o igual que el valor de P y no haya llegado al fin,
        k+=1                           #Incrementa el indice K en 1. K queda en el primer menor o igual a P.
    while S[l]>p:                      #Mientras que el valor de L sea mayor que P,
        l-=1                           #Incrementa indice L en 1. L queda en el primer mayor que P.
    while k<l:
        aux=S[k]
        S[k]=S[l]
        S[l]=aux
        while S[k]<p:
            k+=1
        while S[l]>p:
            l-=1
    aux=S[inicio]
    S[inicio]=S[l]
    S[l]=aux
    return l

def __main__():
    S=[5,8,2,6,4,1,9,7,3]
    quickSort(S,0,len(S)-1)
    print(S)

if __name__=="__main__":
    __main__()