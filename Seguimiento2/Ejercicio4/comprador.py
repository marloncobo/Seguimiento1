class Comprador:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento

    def get_nombre(self):
        return self.__nombre
    def get_documento(self):
        return self.__documento