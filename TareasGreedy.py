class tarea:
    def __init__(self, numero, ganancia, tiempo):
        self.numero = numero
        self.ganancia = ganancia
        self.tiempo = tiempo
    
    def getNumero(self):
        return self.numero

    def getGanancia(self):
        return self.ganancia
    
    def getTiempo(self):
        return self.tiempo

tarea1=tarea(1,50,2)
tarea2=tarea(2,10,1)
tarea3=tarea(3,15,2)
tarea4=tarea(4,30,1)
tareas=[tarea1,tarea2,tarea3,tarea4]

etapa=1
secuencia=[]
mayorGanancia=0
while (etapa<=len(tareas)): #max(tiempoMayorTarea)
    for i in range(len(tareas)):
        if (tareas[i].getTiempo()<=etapa) and (tareas[i].getGanancia()>mayorGanancia):
            numeroMayorGanancia=tareas[i].getNumero()
            mayorGanancia=tareas[i].getGanancia()
            tiempoMayorGanancia=tareas[i].getTiempo()
    secuencia.append((numeroMayorGanancia,mayorGanancia,tiempoMayorGanancia))
    tareas.pop(i)
    etapa+=1
print(secuencia)
