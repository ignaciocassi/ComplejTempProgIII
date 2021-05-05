def MergeSortDyC(S,inicio,fin):
    if inicio<fin:
        mitad=(fin+inicio)//2
        MergeSortDyC(S,inicio,mitad)
        MergeSortDyC(S,mitad+1,fin)
        Merge(S,inicio,fin)

def Merge(S,inicio,fin):
    R=[]
    mitad=(inicio+fin)//2
    i=inicio
    j=mitad+1
    for k in range (0,fin-inicio):
        if (j>fin or S[i]<=S[j] and i<=mitad):
            R.insert(k,S[i])
            i+=1
        else:
            R.insert(j,S[j])
            j=j+1
    for k in range(0,fin-inicio):
        S[inicio+k]=R[k]


def __main__():
    S=[6,3,11,15,4,7,9,2]
    inicio=0
    #Fin: 7
    fin=len(S)-1
    MergeSortDyC(S,inicio,fin)
    print(S)

if __name__=="__main__":
    __main__()
