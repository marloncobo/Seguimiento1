modelo = int(input("Introduzca el modelo: "))

def verificar():
    if modelo == 119 or modelo == 179 or modelo == 189 or modelo == 195 or modelo == 221 or modelo == 780:
        print("El automóvil esta defectuoso, llevar a garantía")
    else:
        print("Su automóvil no está defectuoso")
verificar()