#84. Adivinar palabra desordenada en 3 intentos.
import random
palabras = ["puente", "pantalón"]
palabra = random.choice(palabras)
letras = list(palabra)
random.shuffle(letras)
print(f"Letras desordenadas: {letras}")

acertado = False
for _ in range(3):
    intento = input("Introduce la palabra correcta: ")
    if intento == palabra:
        print("Acertaste")
        acertado = True
        break
if not acertado:
    print("No has acertado ninguno de los intentos")
