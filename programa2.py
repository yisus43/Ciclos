'''
Crea un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''

import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Número de intentos disponibles
intentos = 10

print("¡Bienvenido al juego de adivinar el número!")
print(f"Tienes {intentos} intentos para adivinar el número entre 1 y 100.")

# Bucle principal del juego
while intentos > 0:
    # Pedir al usuario que ingrese un número
    intento_usuario = int(input(f"Te quedan {intentos} intentos. Introduce tu intento: "))

    # Comprobar si el número introducido es correcto
    if intento_usuario == numero_aleatorio:
        print(f"¡Felicidades! Has adivinado el número en {11 - intentos} intentos.")
        break
    elif intento_usuario < numero_aleatorio:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # Restar un intento
    intentos -= 1

# Si se acaban los intentos, mostrar el número aleatorio
if intentos == 0:
    print(f"Has agotado tus intentos. El número correcto era {numero_aleatorio}.")
