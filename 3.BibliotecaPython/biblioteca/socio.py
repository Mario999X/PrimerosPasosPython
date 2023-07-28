# Clase socio | socio() significa heredar de otra clase --> socio(persona) | hijo(padre).
class socio:

    # Contructor de socio, con las variables introducidas | __XX = privado 
    def __init__(self, dni = "", nombre = "", correo = "", telefono = 0, domicilio = "", libros_en_prestamo = []):

        self.__dni = dni
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__libros_en_prestamo = libros_en_prestamo

# Generación de property y setter de las distintas variables.

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,i):
        self.__dni=i

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,i):
        self.__nombre=i
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self,i):
        self.__correo=i
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,i):
        self.__telefono=i

    @property
    def domicilio(self):
        return self.__domicilio
    
    @domicilio.setter
    def domicilio(self,i):
        self.__domicilio=i
    
    @property
    def libros_en_prestamo(self):
        return self.__libros_en_prestamo
    
    @libros_en_prestamo.setter
    def libros_en_prestamo(self,i):
        self.__libros_en_prestamo=i    