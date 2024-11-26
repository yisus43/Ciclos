'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''

# Programa que cuenta números mayores, menores e iguales a 0

# Pedimos al usuario la cantidad de números a introducir
cantidad = int(input("¿Cuántos números deseas introducir? "))

# Inicializamos los contadores
mayores = 0
menores = 0
iguales = 0


for i in range(cantidad):
    numero = float(input(f"Introduce el número {i + 1}: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

print(f"Números mayores que 0: {mayores}")
print(f"Números menores que 0: {menores}")
print(f"Números iguales a 0: {iguales}")