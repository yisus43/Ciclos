'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''
numero_entero = int(input("Introduce un número entero: "))
numero_binario = bin(numero_entero)
print(f"El número {numero_entero} en binario es: {numero_binario[2:]}")