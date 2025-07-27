from partido import Partido
from comprador import Comprador

class Main:
    dinerorecaudado = 0
    disponiblenorte = 100
    disponiblesur = 200
    disponibleVIP = 300
    precionorte = 50000
    preciosur = 50000
    precioVIP = 150000

    partido = Partido("Nacional", "Las Americas", "1 de agosto, 2025")

    while True:
        opcion = input("¿Que desea hacer?\n1. Comprar Boleta \n2. Consultar Disponibilidad\n3. Ver Dinero Recaudado \n4. Salir del Sistema \n")
        if opcion == "1":
            comprador = Comprador(input("Ingrese su nombre: "), input("Ingrese su documento: "))
            localidad = input("Ingrese la localidad :\n1. Norte\n2. Sur\n3. VIP\n4. Salir\n")

            match localidad:
                case "1":
                    boletas = int(input("Ingrese la cantidad de boletas a comprar: "))
                    if boletas <= disponiblenorte:
                        disponiblenorte -= boletas
                        total = boletas*precionorte
                        dinerorecaudado += total
                        print(f"Nombre: {comprador.get_nombre()}\nDocumento: {comprador.get_documento()}\nLocalidad: Norte\nCantidad de boletas: {boletas}\nTotal a pagar: {total}\n")
                    else:
                        print("Boletas agotadas")
                case "2":
                    boletas = int(input("Ingrese la cantidad de boletas a comprar: "))
                    if boletas <= disponiblesur:
                        disponiblesur -= boletas
                        total = boletas * preciosur
                        dinerorecaudado += total
                        print(f"Nombre: {comprador.get_nombre()}\nDocumento: {comprador.get_documento()}\nLocalidad: Sur\nCantidad de boletas: {boletas}\nTotal a pagar: {total}\n")
                    else:
                        print("Boletas agotadas")
                case "3":
                    boletas = int(input("Ingrese la cantidad de boletas a comprar: "))
                    if boletas <= disponibleVIP:
                        disponibleVIP -= boletas
                        total = boletas * precioVIP
                        dinerorecaudado += total
                        print(f"Nombre: {comprador.get_nombre()}\nDocumento: {comprador.get_documento()}\nLocalidad: VIP\nCantidad de boletas: {boletas}\nTotal a pagar: {total}\n")
                    else:
                        print("Boletas agotadas")
                case "4":
                    break
                case _:
                    print("Opción no valida")
        elif opcion == "2":
            totalboletas = disponiblesur + disponibleVIP + disponiblenorte
            print(f"Total de boletas disponibles: {totalboletas}\nLocalidad Norte: {disponiblenorte}\nLocalidad Sur: {disponiblesur}\nLocalidad VIP: {disponibleVIP}\n")
        elif opcion == "3":
            print(f"Dinero Recaudado: {dinerorecaudado}")
        elif opcion == "4":
            break
        else:
            print("Opcion no valida")