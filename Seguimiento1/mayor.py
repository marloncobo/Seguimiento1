num = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
def verificar():
    if num > num2 and num > num3:
        print(f"El número mayor es {num}")
    elif num2 > num and num2 > num3:
        print(f"El número mayor es {num2}")
    elif num3 > num and num3 > num2:
        print(f"El número mayor es {num3}")
    else:
        print("Número no valido")

verificar()