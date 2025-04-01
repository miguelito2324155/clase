#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5.

import random
numero_secreto = random.randint(1, 5)
intento = int(input("Adivina el número (1-5): "))

if intento == numero_secreto:
print("Número acertado")
else:
print("Número no acertado")
