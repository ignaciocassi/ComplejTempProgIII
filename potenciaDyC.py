def calcularPotencia(a,n):
    if n==2:
        b=a
    else:
        b=calcularPotencia(a,n//2)
    return b*b

def __main__():
    print(calcularPotencia(5,4))

if __name__=="__main__":
    __main__()