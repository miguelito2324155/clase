#56. Realiza un programa que gestione un establecimiento de venta de bocadillos.

menu = {
'bocadillos': {
'1': {'nombre': 'Bocadillo de calamares', 'precio': 9},
'2': {'nombre': 'Bocadillo de chistorra', 'precio': 4.5},
'3': {'nombre': 'Bikini de jamón', 'precio': 2.5}
},
'acompanamiento': {
'1': {'nombre': 'Patatas finas', 'precio': 1.5},
'2': {'nombre': 'Patatas gruesas', 'precio': 1.75},
'3': {'nombre': 'Patatas rústicas', 'precio': 2}
},
'bebidas': {
'1': {'nombre': 'Coca cola', 'precio': 2},
'2': {'nombre': 'Acuarius', 'precio': 1.5},
'3': {'nombre': 'Agua', 'precio': 1}
}
}

print("MENÚ")
for categoria, items in menu.items():
print(f"{categoria.upper()}")
for codigo, item in items.items():
print(f"{codigo}. {item['nombre']} - {item['precio']} €")

pedidos = []
otro_pedido = 's'

while otro_pedido.lower() == 's':
pedido = {}
print("\nNuevo pedido:")
for categoria in menu.keys():
eleccion = input(f"Elige {categoria} (1-3 o 0 para ninguno): ")
if eleccion != '0' and eleccion in menu[categoria]:
pedido[categoria] = menu[categoria][eleccion]
pedidos.append(pedido)
otro_pedido = input("¿Deseas realizar otro pedido? (s/n): ")

total = sum(sum(item['precio'] for item in pedido.values()) for pedido in pedidos)
iva = total * 0.1
total_con_iva = total + iva

if 20 <= total <= 30:
descuento = total * 0.05
elif total > 30:
descuento = total * 0.15
else:
descuento = 0

total_con_descuento = total_con_iva - descuento

print("\nRESUMEN")
print(f"Número de pedidos: {len(pedidos)}")
print(f"Total a pagar: {total}")
print(f"Total con iva: {total_con_iva}")
print(f"Precio total con descuento del {int(descuento/total*100 if total > 0 else 0)}%: {total_con_descuento}")
