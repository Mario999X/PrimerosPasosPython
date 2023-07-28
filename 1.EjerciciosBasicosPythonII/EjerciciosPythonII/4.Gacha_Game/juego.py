import personaje as per
import random


lista = [per.personaje("Goku"), per.personaje("Artoria"), per.personaje("Light"), per.personaje("Guts"), per.personaje("Kratos")]

lista_ob = []

def main():
    salir = False
    while salir == False:

        teclado = int(input("""
        0.Salir
        1.Tirar por personaje
        2.Mirar lista propia
        3.Reroll
        """))

        if teclado == 0:
            salir = True

        elif teclado == 1:
            resultado = random.choice(lista)
            print(resultado.nombre)
            lista_ob.append(resultado)
        
        elif teclado == 2:
            if lista_ob == []:
                print("Lista vacia")
            else:
                for i in lista_ob:
                    print(i.nombre)

        elif teclado == 3:
            lista_ob.clear()
            print("Reroll hecho.")

        else: 
            print("Error")

main()