class Cliente:

    def __init__(self, nombre, telefono):
        self.__nombre = nombre
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre
    def get_telefono(self):
        return self.__telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_telefono(self, telefono):
        self.__telefono = telefono