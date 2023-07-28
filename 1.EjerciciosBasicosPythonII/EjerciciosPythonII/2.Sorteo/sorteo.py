import persona as per
import random

lista_personas = []

def main():
    salir = False
    while salir == False:

        teclado = int(input("""
        Introduzca 1 para añadir una persona a la lista.
        2 para realizar el sorteo.
        """))

        if teclado == 1:

            persona = per.persona()
            persona.nombre = str(input("Introduzca el nombre: "))
            persona.edad = int(input("Introduzca su edad: "))
            lista_personas.append(str(persona))
            print(lista_personas)

        elif teclado == 2:

            if lista_personas == []:

                print ("Lista vacia")

            else:

                resultado = random.choice(lista_personas)
                print(resultado)
                salir = True

        else:

            print("Error")

main()
