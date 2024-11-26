'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

ahorros_mensuales = []

for mes in range(1, 13):
    ahorro = float(input(f"Introduce la cantidad ahorrada en el mes {mes}: "))
    ahorros_mensuales.append(ahorro)

total_ahorrado = sum(ahorros_mensuales)

print("\nAhorro mensual:")
for mes, ahorro in enumerate(ahorros_mensuales, start=1):
    print(f"Mes {mes}: ${ahorro:.2f}")

print(f"\nTotal ahorrado al final del año: ${total_ahorrado:.2f}")