# Crea una clase “Saludo” que tenga los métodos: formal, informal y aleatorio. 
# Los métodos pueden aceptar un parámetro (nombre de la persona a saludar) o ninguno (saludo genérico), 
# el método aleatorio imprimirá un saludo aleatorio de una lista de saludos almacenados en la clase

import random

class Saludo:
        
    listaSaludos = ["Otro día, la misma historia", "¿Buenos días? Para tí."]

    def informal(self, nom=""):
        print(f"KLK Manin {nom}")
    
    def formal(self, nom=""):
        print(f"¿Es usted {nom}?")

    def informalRandom(self,sal=[], nom=""):
        saludo=sal[random(0,len(sal)-1)]
        print(f"{saludo} {nom}")