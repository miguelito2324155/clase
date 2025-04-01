#71. Introduce letras en una lista sin duplicados.
lista = []
while True:
    letra = input("Introduce una letra: ").strip().lower()
    if letra not in lista:
        lista.append(letra)
    respuesta = input("¿Deseas repetir? (s/n): ").lower()
    if respuesta != 's':
        break
print(lista)
