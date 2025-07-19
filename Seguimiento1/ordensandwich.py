def verificar():
    tipo = int(input("¿Que tamaño desea? (1/2) "))
    jalapeno = input("¿Desea jalapeño? (s/n) ")
    tocineta = input("¿Desea tocineta? (s/n)? ")
    pavo = input("¿Desea pavo? (s/n)? ")
    queso = input("¿Desea queso? (s/n)? ")
    if tipo == 1:
        tamano = 6000
    elif tipo == 2:
        tamano = 12000
    else:
        print("Opción no valida")
        return

    tocino = 3000 if tocineta == "s" else 0
    pav = 3000 if pavo == "s" else 0
    ques = 2500 if queso == "s" else 0

    print(f"El precio a pagar es: {precio(tamano, tocino, pav, ques)}")

def precio(tamano, tocineta, pavo, queso):
    return tamano + tocineta + pavo + queso

verificar()