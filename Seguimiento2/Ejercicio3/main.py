from Seguimiento2.Ejercicio3.cuentabancaria import Cuentabancaria


class Main:
    cuentaprincipal = Cuentabancaria("Pedro Picapiedra", "122-743", 4000000)
    cuentadestino = Cuentabancaria("Pedro Picapiedra", "542-940", 2000000)

    while True:
        opcion = input("1. Consultar Saldo\n2. Realizar un Depósito (Consignación)\n3. Realizar un Retiro\n4. Realizar una Transferiencia a otra cuenta\n5. Salir\n")
        if opcion == "1":
            print(f"Tu saldo: {cuentaprincipal.getsaldoinicial()}")
        elif opcion == "2":
            cuentaprincipal.depositar(int(input("Ingrese la cantidad a depositar: ")))
        elif opcion == "3":
            if cuentaprincipal.retirar(int(input("Ingrese la cantidad a retirar: "))):
                print("Saldo retirado correctamente")
            else:
                print("No hay saldo suficiente")
        elif opcion == "4":
            cuentaprincipal.transfer(cuentadestino, int(input("Ingrese la cantidad a transfer: ")))
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")