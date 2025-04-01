#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase = "A quién madruga Dios ayuda"
palabras = ["madruga", "Dios", "dios"]

for palabra in palabras:
if palabra in frase:
indice = frase.index(palabra)
print(f"La palabra está en la frase y está en el índice {indice}")
else:
print(f"La palabra no está en la frase")
