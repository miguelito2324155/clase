#83. Juego con múltiples partidas y puntuación.
import random
puntuaciones = []
while True:
    lista = ["casa", "barco", "gato", "perro", "madera"]
    palabra = random.choice(lista)
    intentos = 0
    while True:
        intentos += 1
        intento = input("Adivina la palabra: ")
        if intento == palabra:
            puntuacion = max(9 - intentos, 1)
            puntuaciones.append(puntuacion)
            print("ACERTASTE")
            break
    respuesta = input("¿Deseas otra partida? (s/n): ").lower()
    if respuesta != 's':
        break

total = sum(puntuaciones)
media = total / len(puntuaciones) if puntuaciones else 0
print(f"Puntuación total: {total}")
print(f"Media: {media}")
if total > media:
    print("Tienes buena suerte")
else:
    print("Mejor dedícate al parchís")
