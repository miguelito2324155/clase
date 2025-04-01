#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división). 9 El resultado de la raíz es: 3.0 El resultado de la división es: 1.0 8 El resultado de la raíz es: 2.8 El resultado de la división es: 1.0

import math
numero = float(input("Introduce un número: "))
raiz_cuadrada = math.sqrt(numero)
division = raiz_cuadrada // 2
print(f"El resultado de la raíz es: {raiz_cuadrada}")
print(f"El resultado de la división es: {division}")