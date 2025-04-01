#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
numero = int(input("Introduce un número: "))
contador = 1

while contador <= 10:
resultado = numero * contador
print(resultado)
if resultado >= 40:
print("Fin de programa")
break
contador += 1
