#Haz un programa que adivine la talla de pie y la edad del usuario que lo ejecute. Se basa en un sencillo truco matemático. El programa debe pedir al usuario que realice las siguientes operaciones (las operaciones la tiene que realizar el de cabeza, no el programa):
#Pensar, escribir o apuntar su talla de zapato.
#Multiplicar ese número por 5.
#Sumarle 50.
#Multiplicarlo por 20.
#Sumarle 1022.
#Restarle el año de nacimiento.

numero = input("""Piense en su numero de zapato, y ahora proceda a
multiplicar ese numero por 5; luego sume 50; multiplicalo por 20, 
suma 1022 y reste con su año de nacimiento.
Luego de realizar esa operacion, apunte el numero a continuacion: """)

    # [-2:] desde el penultimo hasta el final | [:2] desde el principio hasta el segundo
print = input ("tu edad es: "+ numero[-2:]+ " y tu talla de pie es: " + numero[:2])
