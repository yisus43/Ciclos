'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

# Programa que calcula la potencia de un número sin usar el operador de potencia


base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (número entero positivo): "))

if exponente < 0:
    print("El exponente debe ser un número entero positivo.")
else:
    resultado = 1  # Inicializamos el resultado en 1


    for _ in range(exponente):
        resultado *= base  # Multiplicamos la base por el resultado

  
    print(f"{base} elevado a {exponente} es: {resultado}")