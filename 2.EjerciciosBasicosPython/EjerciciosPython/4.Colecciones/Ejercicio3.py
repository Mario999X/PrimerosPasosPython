# Crear un programa que almacene con dos opciones: 1. Agregar personas: permite introducir nombres 
# de personas de forma interactiva, 2. Sorteo: devuelve el nombre de una persona al azar.

import random

nombres= ["Alysys", "Shirou"]

salir=False

while salir==False:
    respuesta = input(""" Introduzca 50 para agregar una persona;
    Introduzca 55 para obtener una persona al azar;
    Introduzca 1 para salir:  """)
    if respuesta==str(50):
        nombres.append(input("Introduzca el nombre: "))
    if respuesta==str(55):
        print(nombres[random.randint(0,len(nombres)-1)]) 
    if respuesta==str(1):
        salir=True
        print("See you in Space, Cowboy.") 