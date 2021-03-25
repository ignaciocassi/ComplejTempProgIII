def mayoritario(A,dicc,inicio,fin):
    if (inicio<fin):
        if (A[inicio] in dicc.keys()):
            dicc[A[inicio]]+=1
        else:
            dicc[A[inicio]]=1
        may=mayoritario(A,dicc,inicio+1,fin)
        return may
    else:
        claveMax=max(dicc,key=dicc.get)
        valorMax=dicc[claveMax]
        if valorMax>=(len(A)//2)+1:
            return claveMax
        else:
            return 0       

def __main__():
    A=[4,4,4,4,4,7,1,2]
    dicc=dict()
    print(mayoritario(A,dicc,0,len(A)))

if __name__=="__main__":
    __main__()