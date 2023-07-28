class persona:

    def __init__(self, nombre = "", edad = 0 ):
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        return self.__nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self,edad):
        self.__edad = edad

