#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayor y cuál el menor.
numeros = []
while True:
    num = int(input("Introduce un número (-99 para terminar): "))
    if num == -99:
        break
    numeros.append(num)
if numeros:
    print(f"El número mayor es: {max(numeros)}")
    print(f"El número menor es: {min(numeros)}")
else:
    print("No se introdujeron números")
