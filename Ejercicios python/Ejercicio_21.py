#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo

import math

a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

discriminante = b**2 - 4ac

if discriminante < 0:
print("La raíz no puede ser un valor negativo")
else:
x1 = (-b + math.sqrt(discriminante)) / (2a)
x2 = (-b - math.sqrt(discriminante)) / (2a)
print(f"El valor de x1 es: {x1}")
print(f"El valor de x2 es: {x2}")
