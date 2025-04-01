#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

palabra = input("Introduce una palabra: ").lower()
vocales = []
consonantes = []

for letra in palabra:
if letra in "aeiouáéíóú":
vocales.append(letra)
elif letra.isalpha():
consonantes.append(letra)

print(f"Las vocales de la palabra {palabra} son: {''.join(vocales)}")
print(f"Las consonantes de la palabra {palabra} son: {''.join(consonantes)}")
