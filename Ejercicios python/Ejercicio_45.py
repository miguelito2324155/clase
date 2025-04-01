#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:

palabra = input("Introduce una palabra: ")
vocales = []
consonantes = []

for letra in palabra.lower():
if letra in "aeiouáéíóú":
vocales.append(letra)
elif letra.isalpha():
consonantes.append(letra)

print(f"Las vocales de la palabra {palabra} son: {''.join(vocales)}")
print(f"Las consonantes de la palabra {palabra} son: {''.join(consonantes)}")
