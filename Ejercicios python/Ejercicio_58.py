#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random
numero_secreto = random.randint(1, 5)
intentos = 3

while intentos > 0:
intento = int(input(f"Adivina el número (1-5). Te quedan {intentos} intentos: "))
if intento == numero_secreto:
print("Número acertado")
break
else:
print("Número no acertado")
intentos -= 1
