fisica = int(input("Ingresa la nota de fisica: "))
biologia = int(input("Ingresa la nota de biologia: "))
quimica = int(input("Ingresa la nota de quimica: "))
matematicas = int(input("Ingresa la nota de matematicas: "))
informatica = int(input("Ingresa la nota de informatica: "))

def calificaciones():
    if (fisica < 0 or fisica > 10 or
        biologia < 0 or biologia > 10 or
        quimica < 0 or quimica > 10 or
        matematicas < 0 or matematicas > 10 or
        informatica < 0 or informatica > 10):
        print("Número no valido")
    else:
        resultado()

def promedio ():
    return (fisica+biologia+quimica+matematicas+informatica)/5

def resultado():
    if 0 <= promedio() < 6:
        print(f"Tienes un promedio malo: {promedio()}")
    elif 6 <= promedio() <= 8:
        print(f"Tienes un promedio bueno: {promedio()}")
    elif 8 < promedio() <= 10:
        print(f"Tienes un promedio muy bueno: {promedio()}")

calificaciones()