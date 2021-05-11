def Trasponer(V,K,fin):
    if (K>=fin):
        return V
    else:
        i=K
        f=fin
        while (i>=0):
            aux=V[f]
            V[f]=V[i]
            V[i]=aux
            f=f-1
            i=i-1
        return Trasponer(V,K,fin-(K+1))

def __main__():
    V=[3,5,12,8,9,12,4,7,13,21]
    fin=len(V)-1
    K=2
    Trasponer(V,K,fin)
    print(V)

if __name__=="__main__":
    __main__()