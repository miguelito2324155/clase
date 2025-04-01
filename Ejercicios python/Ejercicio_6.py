#6. A partir del programa 5. Haz que se muestre por pantalla también la frase en el orden inverso en que se han introducido las palabras.

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")
palabra3 = input("Introduce la tercera palabra: ")
palabra4 = input("Introduce la cuarta palabra: ")
palabra5 = input("Introduce la quinta palabra: ")
frase_sin_comas = palabra1 + palabra2 + palabra3 + palabra4 + palabra5
print(frase_sin_comas)
frase_con_comas = ",".join([palabra1, palabra2, palabra3, palabra4, palabra5])
print(frase_con_comas)
frase_inversa_sin_comas = palabra5 + palabra4 + palabra3 + palabra2 + palabra1
print(frase_inversa_sin_comas)
frase_inversa_con_comas = ",".join([palabra5, palabra4, palabra3, palabra2, palabra1])
print(frase_inversa_con_comas)