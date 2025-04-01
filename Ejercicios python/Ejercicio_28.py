#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = input("Introduce un carácter: ")

if len(letra) == 1:
if letra.isalpha():
if letra.isupper():
print("La letra es mayúscula")
else:
print("La letra es minúscula")
elif letra.isdigit():
print("El valor introducido es un número")
else:
print("El valor introducido es un símbolo")
else:
print("¿?")
