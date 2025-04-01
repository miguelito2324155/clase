#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos = float(input("Introduce el número de segundos: "))
minutos = segundos / 60
horas = segundos / 3600
print(f"El número de minutos es: {minutos} y en horas es: {horas}")