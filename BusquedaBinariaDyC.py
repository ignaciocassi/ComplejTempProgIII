def BusquedaBinariaDyC(A,n,inicio,fin):
    if (len(A)==1):
        return A[0]==n
    else:
        mitad=(fin+inicio)//2
        if (n==A[mitad]):
            return True
        else:
            if (n<A[mitad]):
                return BusquedaBinariaDyC(A,n,inicio,mitad-1)
            else:
                return BusquedaBinariaDyC(A,n,mitad+1,fin)


def __main__():
    A=[0,1,2,3,4,5,6,7,8,9]
    print(BusquedaBinariaDyC(A,7,0,len(A)-1))

if __name__=="__main__":
    __main__()