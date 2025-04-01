#55. A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par.

total = 0
operaciones = 0

while total <= 50 or total % 2 == 0:
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
