def kesimo(S,inicio,fin):
    #Busca un A[k]=k, y si existe, devuelve k
    if inicio<=fin:
        k=pivot(S,inicio,fin)
        if S[k]==k:
            return k
        elif S[k]<k:
            return kesimo(S,k+1,fin)
        else:
            return kesimo(S,inicio,k-1)
    else:
        return None

def pivot(S,inicio,fin):                           
    k=(inicio+fin)//2  #Pivot a la mitad
    return k

def __main__():
    S=[-3,-1,0,1,2,5,6]
    k=kesimo(S,0,len(S)-1)
    print(k)

if __name__=="__main__":
    __main__()