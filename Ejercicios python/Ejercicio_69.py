#69. Realiza un programa que permita introducir una cantidad exacta de números, almacenarlos en una lista y presentarlos ordenados.
n = int(input("Introduce la cantidad de números: "))
lista = []
for i in range(n):
    num = int(input(f"Introduce un número ({i+1}/{n}): "))
    lista.append(num)
lista.sort()
print(lista)
