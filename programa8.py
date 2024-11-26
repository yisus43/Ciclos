'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Números pares entre {numero1} y {numero2}:")

for num in range(numero1, numero2 + 1):
    if num % 2 == 0:
        print(num)