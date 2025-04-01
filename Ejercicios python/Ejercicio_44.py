#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’

numeros = []
for i in range(0, 101, 3):
numeros.append(str(i))
print(",".join(numeros))
