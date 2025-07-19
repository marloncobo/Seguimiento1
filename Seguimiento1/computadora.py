emitepitido = input("¿El computador emite un pitido (s/n)? ")
discogira = input("¿El disco gira (s/n)? ")

def verificar():
    if emitepitido == "s" and discogira == "s":
        print("Póngase en contacto con el técnico apoyo ")
    elif emitepitido == "s" and discogira == "n":
        print("Verificar contactos de la unidad ")
    elif emitepitido == "n" and discogira == "n":
        print("Traiga la computadora para repararla en la central ")
    elif emitepitido == "n" and discogira == "s":
        print("Verificar contactos de la unidad ")
    else:
        print("Opción no valida")
verificar()