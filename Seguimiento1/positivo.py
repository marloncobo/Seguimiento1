def verificar():
    if num > 0:
        return True
    else:
        return False

num = int(input("Ingrese un número\n"))
if(verificar()):
    print("Es par")
else:
    print("Es impar")