#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

letra = input("Introduce una letra: ")

if len(letra) == 1:
if letra.isalpha():
if letra.isupper():
print("La letra es mayúscula")
else:
print("La letra es minúscula")
elif letra.isdigit():
print("El valor introducido es un número")
else:
print("¿?")
else:
print("¿?")
