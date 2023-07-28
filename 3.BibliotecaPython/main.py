# ---Gestión de una biblioteca---

import biblioteca.biblioteca as b

biblioteca = b.biblioteca()

 # Método que comienza el proyecto, con un if y unos elif replicamos (casi) el uso de un switch en java.
def main():
    print("ACCEDIENDO AL SISTEMA ADMINISTRATIVO DE LA BIBLIOTECA...")
    salir = False
    while salir == False:
        teclado = int(input("""
        0. Salir
        1. Alta de socio
        2. Baja de socio
        3. Alta de libro
        4. Baja de libro
        5. Prestar un libro
        6. Devolver un libro
        7. Consulta de libros
        8. Consulta de socios
        9. Consulta de préstamos

        Introduzca una opción: """))

        if(teclado == 0):

            print("SALIENDO DEL SISTEMA...")
            salir = True

        elif(teclado == 1):

            biblioteca.añadir_socio()

        elif(teclado == 2):

            biblioteca.borrar_socio()

        elif(teclado == 3):

            biblioteca.añadir_libro()

        elif(teclado == 4):

            biblioteca.borrar_libro()

        elif(teclado == 5):

            biblioteca.prestar_libro()

        elif(teclado == 6):

            biblioteca.devolver_libro()

        elif(teclado == 7):

            biblioteca.consulta_libros()

        elif(teclado == 8):

            biblioteca.consulta_usuarios()

        elif(teclado == 9):

            biblioteca.consulta_prestamos()    

        else:

            print("OPCIÓN INCORRECTA.")    

#  Por si quisieramos importar una clase (en este caso "main", clase y metodo)           
if __name__ == '__main__':
    main()