#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

palabra_secreta = input("Introduce la palabra secreta: ")
longitud = len(palabra_secreta)

for _ in range(longitud):
letra = input("Introduce una letra: ")
posiciones = [str(i) for i, char in enumerate(palabra_secreta) if char == letra]
if posiciones:
print(f"La letra se encuentra en la posición {', '.join(posiciones)}")
else:
print("La letra no existe en la palabra")
