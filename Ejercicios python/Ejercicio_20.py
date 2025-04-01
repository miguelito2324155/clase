#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

num1 = float(input("Introduce el primer número (0-10): "))
num2 = float(input("Introduce el segundo número (0-10): "))

if 0 <= num1 <= 10 and 0 <= num2 <= 10:
if num1 > num2:
print(f"El número {num1} es mayor que el número {num2}")
elif num2 > num1:
print(f"El número {num2} es mayor que el número {num1}")
else:
print("Ambos números son iguales")
else:
print("Uno o los dos números están fuera de los límites establecidos")
