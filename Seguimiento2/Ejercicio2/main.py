from reserva import Reserva
from cliente import Cliente

class Main:
    cliente = Cliente(input("Nombre: "), input("Telefono: "))
    reserva = Reserva(input("Numero de habitaciones: "), input("Cantidad de noches: "), cliente)
    reserva.setcliente(cliente)
    print(f"Resumen Final\n\nNombre: {reserva.getcliente().get_nombre()} - Telefono: {reserva.getcliente().get_telefono()} \nNumero de habitacion: {reserva.getnumerohabitacion()} - Cantidadnoches: {reserva.getcantidadnoche()}\n")

