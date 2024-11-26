'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''

while True:
    limite_inferior = float(input("Introduce el límite inferior del intervalo: "))
    limite_superior = float(input("Introduce el límite superior del intervalo: "))
    
    if limite_inferior < limite_superior:
        break
    else:
        print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")


suma_intervalo = 0
fuera_intervalo = 0
encontrado_limites = False

print("Introduce números (introduce 0 para terminar):")

while True:
    numero = float(input())
    
    if numero == 0:
        break
    if limite_inferior < numero < limite_superior:
        suma_intervalo += numero
    else:
        fuera_intervalo += 1
    
    if numero == limite_inferior or numero == limite_superior:
        encontrado_limites = True

print(f"La suma de los números dentro del intervalo es: {suma_intervalo}")
print(f"Números fuera del intervalo: {fuera_intervalo}")
if encontrado_limites:
    print("Se introdujo al menos un número igual a los límites del intervalo.")
else:
    print("No se introdujo ningún número igual a los límites del intervalo.")