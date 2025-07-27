from Seguimiento2.Ejercicio2.cliente import Cliente


class Reserva:
    def __init__(self, numerohabitacion, cantidadnoche, cliente: Cliente):
        self.__numerohabitacion = numerohabitacion
        self.__cantidadnoche = cantidadnoche
        self.__cliente = cliente

    def getnumerohabitacion(self):
        return self.__numerohabitacion
    def getcantidadnoche(self):
        return self.__cantidadnoche
    def getcliente(self):
        return self.__cliente

    def setnumerohabitacion(self, numerohabitacion):
        self.__numerohabitacion = numerohabitacion
    def setcantidadnoche(self, cantidadnoche):
        self.__cantidadnoche = cantidadnoche
    def setcliente(self, cliente):
        self.__cliente = cliente
