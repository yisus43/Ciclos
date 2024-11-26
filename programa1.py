'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
'''
# Solicitar un número al usuario
n = int(input("Introduce un número para calcular su factorial: "))

# Calcular el factorial utilizando un bucle
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {n} es: {factorial}")
