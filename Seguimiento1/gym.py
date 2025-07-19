dias = int(input("Ingresa el número de dias (15, 30, 90): "))
match dias:
    case 15:
        print("Su recibo mensual es de 18000")
    case 30:
        print("Su recibo mensual es de 35000")
    case 90:
        print("Su recibo mensual es de 86000")
    case _:
        print("Cantidad no valida")