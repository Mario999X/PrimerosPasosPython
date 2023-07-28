class empleado:

    def __init__(self, nombre = "", id = 0):
        self.__nombre = nombre
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id