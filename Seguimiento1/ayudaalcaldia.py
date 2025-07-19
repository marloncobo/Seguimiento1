genero = input("Ingrese su genero (femenino/masculino): ")
edad = int(input("Ingrese su edad: "))

def verificar():
    match genero:
        case "masculino":
            return 40000
        case "femenino":
            if edad > 50:
                return 120000
            elif 30 <= edad <= 50:
                return 100000
            else:
                return 0
        case _:
            return -1

def ayuda():
    resultado = verificar()
    if resultado == -1:
        print("Genero no valido")
    else:
        if edad > 0:
            print(f"Su recibo mensual es de {verificar()}")
        else:
            print("Edad no valido")

ayuda()