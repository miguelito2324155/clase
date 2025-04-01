#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
print(f"El número {num1} es mayor que el número {num2}")
elif num2 > num1:
print(f"El número {num2} es mayor que el número {num1}")
else:
print("Ambos números son iguales")
