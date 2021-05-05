def Ordenado(S):
    L=len(S)
    if L==0:                        #Caso Base 2: S está ordenado porque tiene 1 elem.
        return True
    if L==1:                        #Caso Base 2: S está ordenado porque tiene 1 elem.
        return True
    if L==2:                    #Caso Base 3: S está ordenado porque S[0] < S[1] y tiene 2 elem.
        return S[0]<S[1]           
    else:                       #Subproblema: S tiene más de 2 elem.
        M=L//2
        if S[M-1]<S[M]:
            centro=True
        else:
            centro=False
        R1=Ordenado(S[0:M])
        R2=Ordenado(S[M:L])
        return R1 and R2 and centro    #Devuelve True si las mitades R1 y R2 devuelven True respecticamente.

S=[1,2,3,4,5,6,7,8]
print(Ordenado(S))