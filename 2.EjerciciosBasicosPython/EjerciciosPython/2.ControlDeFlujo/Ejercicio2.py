#Programa que adivine el numero en el que está pensando (entre 0 y 100) 
# el usuario por tanteo (preguntando sucesivamente si es mayor o menor que un número aleatorio de partida)

import random

numeroPensado = False
numMin = 1
numMax = 100

print("Por favor, piense en un numero del 1 al 100")
while numeroPensado == False:
    intentoDeAdivinacion = random.randint(numMin,numMax)
    respuesta = input("¿Es este tu número pensado?: " +str(intentoDeAdivinacion) + " ")
    if respuesta == "Si" or respuesta == "Sí" or respuesta == "si" or respuesta == "sí":
        numeroPensado = True
    else:
        mayor = input("¿El numero es mayor que: " + str(intentoDeAdivinacion) + " ?  ")
        if mayor == "Si" or mayor == "Sí" or mayor == "si" or mayor == "sí":
            numMin = intentoDeAdivinacion
        else:
            numMax = intentoDeAdivinacion

print("Intento de adivinación completado.")                    
