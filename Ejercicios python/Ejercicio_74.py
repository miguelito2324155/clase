#74. Muestra todos los elementos no repetidos entre dos listas.
lista1 = ["casa", "mesa", "sal", "sol", "agua"]
lista2 = ["casa", "luz", "tres", "tren", "sol", "pan"]
repetidas = list(set(lista1) & set(lista2))
no_repetidas = list((set(lista1) | set(lista2)) - set(repetidas))
print(f"Están repetidas: {repetidas}")
print(f"No están repetidas: {no_repetidas}")
