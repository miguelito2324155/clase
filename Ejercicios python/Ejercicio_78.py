#78. Eliminar números específicos de la lista.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
while True:
    valor = input("Introduce el valor que deseas eliminar: ")
    if valor.isdigit():
        if valor in lista1:
            lista1.remove(valor)
            print(lista1)
        else:
            print("El valor no está en la lista.")
    else:
        print("Debe ser un número.")
    respuesta = input("¿Deseas introducir otro valor? (s/n): ").lower()
    if respuesta != 's':
        break
