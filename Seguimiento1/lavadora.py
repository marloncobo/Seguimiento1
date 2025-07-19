tipo = int(input('Ingrese el tipo de lavadora: (1/2)'))
cantidad = int(input('Ingrese la cantidad de lavadoras: '))
horas = int(input('Ingrese la hora: '))
def verificartipo():
    if tipo == 1:
        return 4000
    elif tipo == 2:
        return 3000
def descuento():
    if cantidad >= 3:
        return 0.03
    else:
        return 1
def total():
    total = cantidad*verificartipo()*horas
    if descuento() == 1:
        return total
    else:
        return total*(1-descuento())

print(f"Cantidad de lavadoras: {cantidad}\nTotal a pagar: {total()}")