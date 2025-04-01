#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones: Debe tener una longitud entre 6 y 8 caracteres. Debe contener como mínimo: 2 números mayores o iguales que 1 y menor o igual que 5 2 letras minúsculas 1 letra mayúscula 2 símbolos (*, _, @, &, /, #) 1 número mayor o igual que 6 y menor o igual que 9.
import re
while True:
    password = input("Introduce una contraseña: ")
    if (6 <= len(password) <= 8 and
        len(re.findall(r'[a-z]', password)) >= 2 and
        len(re.findall(r'[A-Z]', password)) >= 1 and
        len(re.findall(r'[1-5]', password)) >= 2 and
        len(re.findall(r'[*_@&/#]', password)) >= 2 and
        len(re.findall(r'[6-9]', password)) >= 1):
        print("Password correcto")
    else:
        print("Password incorrecto")
    respuesta = input("¿Deseas introducir otro password? (s/n): ")
    if respuesta.lower() != 's':
        break
