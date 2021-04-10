def monedasGreedy(v):
    n=0                               #cantidad de monedas utilizadas
    s=0                               #importe total actual cubierto
    i=0                               #indice actual
    monedas=[100,50,25,10,5,1]
    while (s<v and i<len(monedas)):   #Mientras que la sumatoria (s) sea menor que el valor (v) del importe a devolver.
        if (s+monedas[i]<=v):          #Y el indice (i) no llegue a la últ. moneda.
            s+=monedas[i]             #Si la sumatoria más la moneda actual, no supera el valor del importe a devolver.
            n+=1                      #Cuento una moneda más.
        else:                         #Si supera o iguala al valor del importe a devolver.
            i+=1                      #Avanza a la siguiente moneda (de menor valor).
    if (i<len(monedas)):              #Si el índice no llego a salir del arreglo de monedas, no me quedé sin monedas
        return n                      #Devuelvo n, (cantidad de monedas utilizadas)
    else:                             #Sino, si me quede sin monedas, no tiene solución.
        return None                                  
    
print(monedasGreedy(177))