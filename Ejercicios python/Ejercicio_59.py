#59. Diseña un programa que "piense" un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo.

import random
numero_secreto = random.randint(1, 1000)
intentos = 0

while True:
intento = int(input("Introduce un valor comprendido entre 1 y 1000: "))
intentos += 1
if intento == numero_secreto:
print(f"Acertaste, has realizado {intentos} intentos")
break
elif intento < numero_secreto:
print("El número que has introducido es menor")
else:
print("El número que has introducido es mayor")
