#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While

repetir = 's'
while repetir.lower() == 's':
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
print(f"El resultado de la suma es: {suma}")
repetir = input("Deseas repetir la operación s/n: ")

print("Programa finalizado")
