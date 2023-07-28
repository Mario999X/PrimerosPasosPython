# Reescribe el ejercicio 3 del apartado “Colecciones” utilizando una función para presentar el menú y recibir la opción seleccionada.

import random

def mostrar_menu():
        return str( input(""" Introduzca 50 para agregar una persona;
    Introduzca 55 para obtener una persona al azar;
    Introduzca 1 para salir:  """))

nombres= ["Alysys", "Shirou"]

salir=False

while salir==False:
    resultado = mostrar_menu()
    if resultado==str(50):
        nombres.append(input("Introduzca el nombre: "))
    if resultado==str(55):
        print(nombres[random.randint(0,len(nombres)-1)]) 
    if resultado==str(1):
        salir=True
        print("See you in Space, Cowboy.")   