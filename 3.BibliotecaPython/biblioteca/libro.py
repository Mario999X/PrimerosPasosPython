# Clase libro | libro() significa heredar de otra clase --> libro(biblioteca) | hijo(padre).
class libro:

    # Contructor de libro, con las variables introducidas | __XX = privado 
    def __init__(self, isbn = "", titulo = "", autor = "", genero = "", portada = "", sinopsis = "", ejemplares = 0):
        self.__isbn=isbn
        self.__titulo=titulo
        self.__autor=autor
        self.__genero=genero
        self.__portada=portada
        self.__sinopsis=sinopsis
        self.__ejemplares=ejemplares

# Generación de property y setter de las distintas variables.

    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self,a):
        self.__isbn=a

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,a):
        self.__titulo=a
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,a):
        self.__autor=a
    
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self,a):
        self.__genero=a

    @property
    def portada(self):
        return self.__portada
    
    @portada.setter
    def portada(self,a):
        self.__portada=a
    
    @property
    def sinopsis(self):
        return self.__sinopsis
    
    @sinopsis.setter
    def sinopsis(self,a):
        self.__sinopsis=a
    
    @property
    def ejemplares(self):
        return self.__ejemplares
    
    @ejemplares.setter
    def ejemplares(self,a):
        self.__ejemplares=a

