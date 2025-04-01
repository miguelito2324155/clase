#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))
cociente = dividendo / divisor
resto = dividendo % divisor
if dividendo % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"
print(f"El cociente es: {cociente}")
print(f"El resto es: {resto}")
print(f"El dividendo es {paridad}")