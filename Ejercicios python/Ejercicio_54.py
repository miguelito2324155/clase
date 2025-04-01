#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice.

total = 0
operaciones = 0

while total <= 50:
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
total += suma
operaciones += 1
print(f"El resultado de la suma es: {suma}")
if operaciones == 1:
print(f"El total acumulado es: {total} y llevas {operaciones} operación realizada")
else:
print(f"El total acumulado es: {total} y llevas {operaciones} operaciones realizadas")

print("Fin del programa")

