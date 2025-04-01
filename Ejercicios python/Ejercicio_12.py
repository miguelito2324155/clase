#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
import math
lado = float(input("Introduce el valor del lado: "))
base_menor = float(input("Introduce el valor de la base menor: "))
base_mayor = float(input("Introduce el valor de la base mayor: "))
altura = float(input("Introduce el valor de la altura: "))
perimetro = 2 * lado + base_menor + base_mayor
area = ((base_menor + base_mayor) / 2) * altura
print(f"El perímetro es: {perimetro}")
print(f"El área es: {area}")