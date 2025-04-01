#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

n = int(input("Introduce un número: "))
suma = 0

for i in range(1, n + 1):
suma += i

print(f"La suma total de números naturales es: {suma}")
