class Partido:
    def __init__(self, equipolocal, equipovisitante, fecha):
        self.__equipolocal = equipolocal
        self.__equipovisitante = equipovisitante
        self.__fecha = fecha

    def get_equipolocal(self):
        return self.__equipolocal
    def get_equipovisitante(self):
        return self.__equipovisitante
    def get_fecha(self):
        return self.__fecha