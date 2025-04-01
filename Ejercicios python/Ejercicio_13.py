#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.


lado = float(input("Introduce el valor del lado del cubo: "))
area = 6 * (lado ** 2)
volumen = lado ** 3
print(f"El área del cubo es: {area}")
print(f"El volumen del cubo es: {volumen}")