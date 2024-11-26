'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
# Programa que identifica si los caracteres son vocales o no

while True:
    # Pedimos al usuario que introduzca un carácter
    caracter = input("Introduce un carácter (espacio para terminar): ")

    # Verificamos si el carácter es un espacio para terminar el programa
    if caracter == " ":
        print("Programa terminado.")
        break

    # Verificamos si se ha introducido un único carácter
    if len(caracter) == 1:
        # Verificamos si el carácter es una vocal
        if caracter.lower() in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")
    else:
        print("Por favor, introduce solo un carácter.")


