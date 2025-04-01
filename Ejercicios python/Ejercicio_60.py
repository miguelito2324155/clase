#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while

numero = int(input("Introduce un número: "))
contador = 1

while contador <= 10:
print(numero * contador)
contador += 1
