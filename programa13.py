'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
meses = 20
pago_mensual = 10
total_pagado = 0


for mes in range(1, meses + 1):
    total_pagado += pago_mensual
    print(f"Mes {mes}: Pago = {pago_mensual} euros")
    pago_mensual *= 2
print(f"\nTotal pagado después de {meses} meses: {total_pagado} euros")