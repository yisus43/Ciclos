'''
Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''


for i in range(1, 6):
    print(f"Tabla de multiplicar del {i}:")
    # Iteramos sobre los multiplicadores del 1 al 10
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # Línea en blanco para separar las tablas