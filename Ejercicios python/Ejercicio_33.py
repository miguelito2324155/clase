#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años

frase = "No hay mal que dure cien años".lower()
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in frase:
if letra in vocales:
vocales[letra] += 1

print(f"El número de a es {vocales['a']} el número de e es {vocales['e']} el número de i es {vocales['i']} el número de o es {vocales['o']} y el número de u es {vocales['u']}")
