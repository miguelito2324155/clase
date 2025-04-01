#70. Crea dos listas (lista1 y lista2) y muéstralas en orden ascendente y descendente.
lista1 = []
n = int(input("Introduce la cantidad de palabras: "))
for i in range(n):
    palabra = input(f"Introduce {i+1}ª palabra: ")
    lista1.append(palabra)
lista2 = lista1.copy()
lista1.sort()
lista2.sort(reverse=True)
print(f"lista1 contiene: {lista1}")
print(f"lista2 contiene: {lista2}")
