#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

operador1 = float(input("Introduce el primer operando: "))
operador2 = float(input("Introduce el segundo operando: "))
suma = operador1 + operador2
resta = operador1 - operador2
multiplicacion = operador1 * operador2
division = operador1 / operador2
exponente = operador1 ** operador2
division_entera = operador1 // operador2
modulo = operador1 % operador2
print(f"La suma de operador1 y operador2 es: {suma}")
print(f"La resta de operador1 y operador2 es: {resta}")
print(f"La multiplicación de operador1 y operador2 es: {multiplicacion}")
print(f"La división de operador1 y operador2 es: {division:.2f}")
print(f"El exponente de operador1 y operador2 es: {exponente}")
print(f"La división entera de operador1 y operador2 es: {division_entera}")
print(f"El módulo de operador1 y operador2 es: {modulo}")