#11. Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva por pantalla en el área y el perímetro.

lado = float(input("Introduce el valor del lado del cuadrado: "))
perimetro = 4 * lado
area = lado * lado
print(f"El perímetro del cuadrado es: {perimetro}")
print(f"El área del cuadrado es: {area}")