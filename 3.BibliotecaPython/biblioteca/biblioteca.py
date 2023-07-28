import biblioteca.libro as lib
import biblioteca.socio as soc

# Clase biblioteca | biblioteca() significa heredar de otra clase --> biblioteca(instituto) | hijo(padre).
class biblioteca:

    # Contructor de libro, con las variables introducidas | __XX = privado
    def __init__(self, lista_libros = [], lista_usuarios = []):
        self.__lista_libros=lista_libros
        self.__lista_usuarios=lista_usuarios

    # Método que añade un socio a la lista de usuarios.
    def añadir_socio(self):
        socio = soc.socio()
        socio.dni = str(input("Introduzca su DNI: "))
        socio.nombre = str(input("Introduzca su nombre: "))
        socio.correo = str(input("Introduzca su correo: "))
        socio.telefono = int(input("Introduzca su telefono: "))
        socio.domicilio = str(input("Introduzca su domicilio: "))
        socio.__libros_en_prestamo = []
        self.__lista_usuarios.append(socio)
        print ("El usuario: " + socio.nombre + " ha sido añadido a la biblioteca del centro.")

    # Método que elimina un socio, enlazado a su DNI, recorriendo la lista de usuarios.
    def borrar_socio(self):
        decision_borrar_soc = str(input("Introduzca el DNI del socio a eliminar: "))
        for i in self.__lista_usuarios:
            if (i.dni == decision_borrar_soc):
                self.__lista_usuarios.remove(i)
                print ("El socio ha sido eliminado con éxito.")
            else:
                print("ERROR, introduzca un DNI correcto.")    

    # Método que añade un libro a la lista de libros.
    def añadir_libro(self):
        libro = lib.libro()
        libro.isbn = str(input("Introduzca el ISBN del libro: "))
        libro.titulo = str(input("Introduzca el título: "))
        libro.autor = str(input("Introduzca su autor: "))
        libro.genero = str(input("Introduzca el género del libro: "))
        libro.portada = str(input("Introduzca descripción simple de la portada: "))
        libro.sinopsis = str(input("Introduzca la sinopsis: "))
        libro.ejemplares = int(input("Introduzca el número de ejemplares: "))
        self.__lista_libros.append(libro)
        print ("El libro " + libro.titulo + " ha sido introducido con éxito.")

    # Método que elimina un libro, enlazado a su ISBN, recorriendo la lista de libros.
    def borrar_libro(self):
        decision_borrar_lib = input ("Introduzca el ISBN del libro a eliminar: ")
        for i in self.__lista_libros:
            if (i.isbn == decision_borrar_lib):
                self.__lista_libros.remove(i)
                print("El libro ha sido eliminado con éxito.")
            else:
                print("ERROR, introduzca un ISBN correcto.")

    # Método que añade un libro, enlazado al ISBN, a la lista de libros en préstamo de cada usuario, representado por su DNI.
    def prestar_libro(self):
        decision_elegir_usuario_pl = str(input("Introduzca un DNI de usuario existente: "))
        for i in self.__lista_usuarios:
            if (i.dni == decision_elegir_usuario_pl):
                meter_libro = str(input("Introduzca el ISBN del libro a prestar: "))
                i.__libros_en_prestamo.append(meter_libro)
                print("El usuario: " + i.nombre + " ha recibido el libro.")
            else:
                print("ERROR, ese usuario no existe.")

    # Método que elimina un libro, enlazado a su título e ISBN, de la lista de libros en préstamo de cada usuario, representado por su DNI.
    def devolver_libro(self):
        decision_elegir_usuario_dl = str(input("Introduzca un DNI de usuario existente: "))
        for i in self.__lista_usuarios:
            if (i.dni == decision_elegir_usuario_dl and str(i.__libros_en_prestamo) != None):
                devolver_libro = str(input("Introduzca el ISBN del libro a devolver: "))
                i.__libros_en_prestamo.remove(devolver_libro)
                print("El usuario: " + i.nombre + " ha devuelto el libro.")
            else:
                print("ERROR, socio no existente o el usuario no tiene libros en préstamo.")   
        
    # Método que recorre la lista de libros e imprime por pantalla el título y su ISBN.
    def consulta_libros(self):
        for i in self.__lista_libros:
            print ("Titulo: " + i.titulo + " | ISBN: " + i.isbn)

    # Método que recorre la lista de usuarios e imprime por pantalla el nombre y su DNI.
    def consulta_usuarios(self):
        for i in self.__lista_usuarios:
            print ("Nombre: " + i.nombre + " con DNI: "+ i.dni + " | DNI: " + i.dni)    

    # Método que recorre la lista de usuarios e imprime por pantalla el nombre, su DNI y los libros en préstamo (ISBN).
    def consulta_prestamos(self):
        for i in self.__lista_usuarios:
            if (i.__libros_en_prestamo != []):
                print("Socio: " + i.nombre + " con DNI: "+ i.dni + " | Libros en préstamo (ISBN): " + str(i.__libros_en_prestamo))      

                 
