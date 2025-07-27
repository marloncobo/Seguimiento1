class Monitor:
    __horasAcumuladas = 0
    def __init__(self, name, codigoEstudiante, eventoAsignado):
        self.__name = name
        self.__codigoEstudiante = codigoEstudiante
        self.__eventoAsignado = eventoAsignado

    def registrarHoras(self, horas):
        self.__horasAcumuladas += horas

    def verificarEstado(self):
        if self.__horasAcumuladas >=8:
            return "Horas completas"
        else:
            return "Horas pendientes"

    def get_name(self):
        return self.__name
    def get_codigoEstudiante(self):
        return self.__codigoEstudiante
    def get_eventoAsignado(self):
        return self.__eventoAsignado
    def get_horasAcumuladas(self):
        return self.__horasAcumuladas