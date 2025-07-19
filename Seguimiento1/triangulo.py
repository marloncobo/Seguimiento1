angulo1 = int(input("Digite su primer angulo: "))
angulo2 = int(input("Digite su segundo angulo: "))
angulo3 = int(input("Digite su tercer angulo: "))

def verificar():
    suma = angulo1 + angulo2 + angulo3
    if suma == 180:
        return True
    else:
        return False

def main():
    resultado = verificar()
    if resultado:
        print("El triangulo es valido")
    else:
        print("El triangulo no es valido")

main()