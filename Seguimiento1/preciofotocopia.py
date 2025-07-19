numcopia = int(input("Numero de copias: "))

def precioporcopia():
    if 0 < numcopia < 500:
        return 120
    elif 500 <= numcopia < 750:
        return 100
    elif 750 <= numcopia < 1000:
        return 80
    elif 1000 <= numcopia:
        return 50
    else:
        return 0

def preciototal():
    resultado = precioporcopia()
    if resultado == 0:
        print("Cantidad no valida")
    else:
        preciototal = resultado * numcopia
        print(f"El precio por copia: {precioporcopia()}\nNúmero de copias: {numcopia}\nTotal a pagar: {preciototal}")
preciototal()