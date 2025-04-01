#76. Ordenar letras y números de forma correcta.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
numeros = sorted([x for x in lista1 if x.isdigit()], key=lambda x: int(x))
letras = sorted([x for x in lista1 if x.isalpha()], key=lambda x: x.lower())

opcion = int(input("Introduce 1 (ascendente) o 2 (descendente): "))
if opcion == 2:
    numeros = sorted(numeros, key=lambda x: int(x), reverse=True)
    letras = sorted(letras, key=lambda x: x.lower(), reverse=True)

print(numeros)
print(letras)
