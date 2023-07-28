# Crear un programa “Diccionario” que permita consultar definiciones, agregar nuevas palabras 
# con su definición o eliminar palabras.


salir=False
diccionario = {"Hello":"hola", "Comeback":"Regreso"}
while salir==False:
    resultado = input(
 """Introduzca 10 para consultar una definición
    Introduzca 20 para agregar palabras
    Introduzca 30 para eliminar palabras
    Introduzca 40 para salir""")
    if resultado==str(10):
       print(str(diccionario.get(input("Escriba la palabra en inglés para obtener su traducción"))))
    if resultado==str(20):
        clave= input("Introduzca la palabra en inglés")
        valor = input ("Introduzca la palabra en español")
        diccionario[clave]=valor
        print("Registro exitoso")
    if resultado==str(30):
        diccionario.pop(str(input("¿Qué palabra en inglés desea eliminar?")))
    if resultado==str(40):
        salir=True
        print("See you in Hell")