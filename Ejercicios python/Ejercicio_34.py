#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente

var_numero = "6734" # Error 1: debe ser string para usar len()
var_suma = 0
var_longitud = len(var_numero) # Error 2: len() aplicado correctamente

#Error 3: índices en Python empiezan en 0
var_suma = int(var_numero[0]) + int(var_numero[1]) + int(var_numero[2]) + int(var_numero[3])

#Error 4: operador módulo % en lugar de división //
if var_suma % 2 == 0:
print(f'El valor de {var_suma} es par')
else:
print(f'El valor de {var_suma} es impar')
