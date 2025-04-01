#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math
diametro = float(input("Introduce el diámetro del círculo: "))
radio = diametro / 2
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)
print(f"El perímetro del círculo es: {perimetro:.1f}")
print(f"El área del círculo es: {area:.1f}")