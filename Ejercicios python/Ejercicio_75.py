#75. Cuenta números, letras y mayúsculas en una lista.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
numeros = [x for x in lista1 if x.isdigit()]
letras = [x for x in lista1 if x.isalpha()]
mayusculas = [x for x in letras if x.isupper()]
suma_numeros = sum(int(x) for x in numeros)

print(f"Número de valores: {len(lista1)}")
print(f"Cantidad de números: {len(numeros)}")
print(f"Cantidad de letras: {len(letras)}")
print(f"Cantidad de mayúsculas: {len(mayusculas)}")
print(f"Suma total de números: {suma_numeros}")
