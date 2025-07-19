nombre = input("Ingrese el nombre: ")
horas = int(input("Ingrese la cantidad de horas: "))

def salario():
    if horas >=1 and horas <=10:
        return 30000
    elif horas > 10:
        return 33000
    else:
        return "Cantidad no valida"

def pago ():
    return salario()*horas

print(f'Señor {nombre} el número de horas es {horas} y su salario equivale a {pago()}')