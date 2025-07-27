from Monitor import Monitor

monitor1 = Monitor("Ana Pérez", "101", "Feria Universitaria - Unicentro")
monitor2 = Monitor("Carlos Rojas", "102", "Visita Colegio San Luis Rey")
monitor3 = Monitor("Pepito Morales", "103", "ExpoU")
monitor4 = Monitor("Roberto Gomez", "104", "Visita a centro de rehabilitacion")
monitor5 = Monitor("Julano Fino", "105", "Visita al coliceo")

while True:
    pregunta =  int(input("1. Registrar Horas de un Monitor \n2. Ver Estado de Todos los Monitores \n3. Salir del Sistema\n"))
    if pregunta == 1:
        seleccionarmonitor = input("Seleccione el monitor\n1. Ana Pérez\n2. Carlos Rojas\n3. Pepito Morales\n4. Roberto Gomez\n5. Julano Fino\n6. Salir del Sistema\n")
        if seleccionarmonitor == "6":
            exit()
        horas = int(input("Selecciona la hora de la monitor: "))
        match seleccionarmonitor:
            case "1":
                monitor1.registrarHoras(horas)
                print(f"Las horas han sido registradas exitosamente\nEl monitor {monitor1.get_name()} - Lleva {monitor1.get_horasAcumuladas()} horas\n\n")
            case "2":
                monitor2.registrarHoras(horas)
                print(f"Las horas han sido registradas exitosamente\nEl monitor {monitor2.get_name()} - Lleva {monitor2.get_horasAcumuladas()} horas\n\n")
            case "3":
                monitor3.registrarHoras(horas)
                print(f"Las horas han sido registradas exitosamente\nEl monitor {monitor3.get_name()} - Lleva {monitor3.get_horasAcumuladas()} horas\n\n")
            case "4":
                monitor4.registrarHoras(horas)
                print(f"Las horas han sido registradas exitosamente\nEl monitor {monitor4.get_name()} - Lleva {monitor4.get_horasAcumuladas()} horas\n\n")
            case "5":
                monitor5.registrarHoras(horas)
                print(f"Las horas han sido registradas exitosamente\nEl monitor {monitor5.get_name()} - Lleva {monitor5.get_horasAcumuladas()} horas\n\n")
            case _:
                print("Opcion no valida")
    elif pregunta == 2:
        print(f"Nombre del monitor: {monitor1.get_name()} - Horas cumplidas: {monitor1.get_horasAcumuladas()} - Estado del monitor: {monitor1.verificarEstado()}\n"
              f"Nombre del monitor: {monitor2.get_name()} - Horas cumplidas: {monitor2.get_horasAcumuladas()} - Estado del monitor: {monitor2.verificarEstado()}\n"
              f"Nombre del monitor: {monitor3.get_name()} - Horas cumplidas: {monitor3.get_horasAcumuladas()} - Estado del monitor: {monitor3.verificarEstado()}\n"
              f"Nombre del monitor: {monitor4.get_name()} - Horas cumplidas: {monitor4.get_horasAcumuladas()} - Estado del monitor: {monitor4.verificarEstado()}\n"
              f"Nombre del monitor: {monitor5.get_name()} - Horas cumplidas: {monitor5.get_horasAcumuladas()} - Estado del monitor: {monitor5.verificarEstado()}\n\n")
    elif pregunta == 3:
        print("Gracias por usar el programa")
        exit()
    else:
        print("Opcion no valida")