Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
... 
... num_notas = int(input("Introduce el número de notas que deseas introducir: "))
... 
... for _ in range(num_notas):
... nota = float(input("Introduce la nota: "))
... if nota >= 5:
... print("Asignatura aprobada")
... else:
