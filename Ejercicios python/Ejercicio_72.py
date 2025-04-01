#72. Ignora vocales acentuadas como duplicados.
vocales = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}
lista = []
while True:
    letra = input("Introduce una letra: ").strip().lower()
    letra_normalizada = letra.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    if letra_normalizada not in [l.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') for l in lista]:
        lista.append(letra)
    respuesta = input("¿Deseas repetir? (s/n): ").lower()
    if respuesta != 's':
        break
print(lista)
