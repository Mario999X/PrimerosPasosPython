#Crear un programa que almacene nombres de personas, tras introducir un nombre nuevo 
# mostrará un conteo de los nombres que tienen 5 o más caracteres y 
# preguntará si desea introducir un nuevo nombre o salir del programa.


listaNombre = []
contador = 0

salir = False
while salir == False:
    nombre = str(input("Introduzca un nombre | Si desea salir, pulse 66: "))
    if nombre == "66":
        salir = True 
    else:
        listaNombre.append(nombre)   
        
        if len(nombre) > 5:
            contador =+1             # esto es equivalente a contador = contador +1
            print(contador)


