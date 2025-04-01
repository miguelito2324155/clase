#82. Adivinar palabra secreta hasta acertar.
import random
lista = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
palabra_secreta = random.choice(lista)
while True:
    intento = input("Introduce la palabra secreta: ")
    if intento == palabra_secreta:
        print("ACERTASTE")
        break
    else:
        print("SIGUE JUGANDO")
