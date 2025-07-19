import random

jugador = []
maquina = []

def generarcarta ():
    numero = random.randint(1, 10)
    return numero

def ganador ():
    if sum(jugador) < sum(maquina):
        print("La maquina ha ganado")
    if sum(jugador) > sum(maquina):
        print("Has ganado")
    if sum(jugador) == sum(maquina):
        print("Ha sido un empate")
    if sum(jugador) > 21:
        print("Te has pasado ha ganado, la maquina")
    if sum(maquina) > 21:
        print("La maquina se ha pasado, has ganado ")

def mostrarcartas ():
    print(f"Tus cartas son: {jugador}\nLas cartas de la maquina son: {maquina}")

opcion = input("¿Quieres jugar? (s/n)\n")
if opcion == "s":
    jugador.append(generarcarta())
    maquina.append(generarcarta())
    print(f"Tu primera carta es: {jugador[0]}\nLa primera carta de la maquina es: {maquina[0]}")
    mostrarcartas()
    opcion2 = input("¿Quieres seguir? (s/n)\n")
    if opcion2 == "s":
        jugador.append(generarcarta())
        maquina.append(generarcarta())
        print(f"Tu segunda carta es: {jugador[1]}\nLa segunda carta de la maquina es: {maquina[1]}")
        print(f"Llevas un total de: {sum(jugador)}\nLa maquina lleva un total de: {sum(maquina)}")
        mostrarcartas()
        opcion3 = input("¿Quieres seguir? (s/n)\n")
        if opcion3 == "s":
            jugador.append(generarcarta())
            maquina.append(generarcarta())
            print(f"Tu ultima carta es: {jugador[2]}\nLa ultima carta de la maquina es: {maquina[2]}")
            print(f"Llevas un total de: {sum(jugador)}\nLa maquina lleva un total de: {sum(maquina)}")
            mostrarcartas()
            ganador()
        elif opcion3 == "n":
            ganador()
    elif opcion2 == "n":
        ganador()