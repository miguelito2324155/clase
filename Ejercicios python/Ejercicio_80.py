#80. Determinar si un número es decimal.
entrada = input("Introduce un valor: ")
try:
    num = float(entrada)
    if '.' in entrada and len(entrada.split('.')[1]) > 0:
        print("Es un número con decimales")
    else:
        print("No es un número con decimales")
