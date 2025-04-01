#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10

num_notas = int(input("Introduce el número de notas que deseas introducir: "))

for _ in range(num_notas):
nota = float(input("Introduce la nota: "))
if nota < 0 or nota > 10:
print("Has introducido una nota equivocada")
elif nota >= 5:
print("Asignatura aprobada")
else:
print("Asignatura suspendida")
