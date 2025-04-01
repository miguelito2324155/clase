#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el númerode veces que se repite cada número.
import random
resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for _ in range(100):
    dado = random.randint(1, 6)
    resultados[dado] += 1
for numero, cantidad in resultados.items():
    print(f"{numero}: {cantidad}")
