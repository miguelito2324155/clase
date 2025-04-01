#8. programa que pida un número de horas y muestre por pantalla los minutos y segundos

horas = float(input("Introduce el número de horas: "))
minutos = horas * 60
segundos = horas * 3600
print(f"El número de minutos es: {minutos} y en segundos es: {segundos}")