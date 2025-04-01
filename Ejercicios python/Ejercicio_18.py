#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
menores = int(input("Introduce el número de menores: "))
adultos = int(input("Introduce el número de adultos: "))
precio_base = 12
descuento_menor = 0.5 
descuento_adulto = 0.1
precio_menor = precio_base * (1 - descuento_menor)
precio_adulto = precio_base * (1 - descuento_adulto)
total_menores = menores * precio_menor
total_adultos = adultos * precio_adulto
print(f"El precio total del cine para {menores} menor/es es: {total_menores}")
print(f"El precio total del cine para {adultos} adulto/s es: {total_adultos}")
