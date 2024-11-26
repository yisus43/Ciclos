'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

contador = 0
acumulador = 0

for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    acumulador += numero 
    contador += 1 


if contador > 0:
    promedio = acumulador / contador
    print(f"El promedio de los {contador} números ingresados es: {promedio:.2f}")
else:
    print("No se ingresaron números.")