#73. Encuentra elementos repetidos entre dos listas.
lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]
repetidas = list(set(lista1) & set(lista2))
no_repetidas = list(set(lista2) - set(lista1))
print(f"Están repetidas: {repetidas}")
print(f"No están repetidas: {no_repetidas}")
