# Reescribe el ejercicio 3 del apartado “Colecciones” con orientación a objetos.


import random

class Mostrador_de_nombres:

    def __init__(self, nombres= ["Alysys", "Shirou"]) -> None:
        self.__nombres=nombres

    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self,a):
        self.__nombres=a

    def mostrar_menu(self):
            return str( input(""" Introduzca 50 para agregar una persona;
    Introduzca 55 para obtener una persona al azar;
    Introduzca 1 para salir:  """))


    def randomNames(self):
        salir=False
        while salir==False:
            resultado = self.mostrar_menu()
            if resultado==str(50):
                self.nombres.append(input("Introduzca el nombre: "))
            if resultado==str(55):
                print(self.nombres[random.randint(0,len(self.nombres)-1)]) 
            if resultado==str(1):
                salir=True
                print("See you in Space, Cowboy.")   

class App:
    mostrador= Mostrador_de_nombres()
    mostrador.randomNames()