#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

frase = "A quién madruga Dios ayuda".lower()
palabras = ["madruga", "Dios", "dios"]

for palabra in palabras:
if palabra.lower() in frase:
indice = frase.index(palabra.lower())
print(f"La palabra está en la frase y está en el índice {indice}")
else:
print(f"La palabra no está en la frase")
