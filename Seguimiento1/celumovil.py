tipooperador = input("Ingrese el operador movil al que pertenece: ")
minutosconsumidos = int(input("Ingrese la cantidad de minutos consumidos: "))
paquete = input("¿Quiere un paquete de datos? (s/n) ")

cargofijo = 0
mininternacional = 0
paqdatos = 0

def verificar():
    global cargofijo, mininternacional, paqdatos, tipooperador
    match tipooperador.lower():
        case "tigo":
            cargofijo = 45000
            mininternacional = 200
            paqdatos = 12000
            return True
        case "claro":
            cargofijo = 30000
            mininternacional = 100
            paqdatos = 18000
            return True
        case "movistar":
            cargofijo = 40000
            mininternacional = 250
            paqdatos = 8000
            return True
        case _:
            return False

def verificarpaquete():
    global paqdatos
    if paquete == "s":
        verificar()
    else:
        verificar()
        paqdatos = 0

def precio():
    return cargofijo + mininternacional*minutosconsumidos + paqdatos

def menu():
    if verificar():
        verificarpaquete()
        print(f"el total a pagar es: {precio()}")
    else:
        print("Operador no valido")
menu()