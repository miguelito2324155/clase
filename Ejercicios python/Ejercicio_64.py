#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:

pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
total = 0
while True:
    num = int(input("Introduce un número (-99 para terminar): "))
    if num == -99:
        break
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1
    total += num
print(f"RESUMEN")
print(f"El número de pares es {pares}")
print(f"El número de impares es {impares}")
print(f"El número de positivos es {positivos}")
print(f"El número de negativos es {negativos}")
print(f"El número de ceros es {ceros}")
print(f"El total es {total}")
