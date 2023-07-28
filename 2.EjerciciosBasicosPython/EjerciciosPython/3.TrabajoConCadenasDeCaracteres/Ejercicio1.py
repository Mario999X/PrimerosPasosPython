#Solicitar una oración por teclado y realizar las siguientes operaciones sobre ella:
# Longitud de la cadena.
# Mostrar espacios en blanco se ingresaron.
# Mostrar toda la oración en letras mayúsculas.
# Duplicar el contenido de la cadena.
# Dividir la cadena en una lista de palabras y recorrerla mostrándola y numerando cada palabra.



frase = input ("Introduzca una frase: ")

longitudFrase = print (len(frase))
espacios = frase.count(" ")
str(espacios)
print(espacios)

print(frase.upper())

print(frase *2)

listado = frase.split()
cont=0
for i in listado:
    cont=cont+1
    print(cont)
    print(i)
   
