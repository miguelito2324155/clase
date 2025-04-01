#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While

repetir = 's'
total = 0
repeticiones = 0

while repetir.lower() == 's':
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
total += suma
repeticiones += 1
print(f"El resultado de la suma es: {suma}")
repetir = input("Deseas repetir la operación s/n: ")

print("Resumen:")
print(f"La suma total es: {total} y el número de repeticiones es: {repeticiones}")
