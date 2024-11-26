'''
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
'''
import math

# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False  
    if num <= 3:
        return True  
    if num % 2 == 0 or num % 3 == 0:
        return False  
    
    
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    
    return True


numero = int(input("Introduce un número entero: "))

# Verificamos si el número es primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")