'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def primeros_n_primos(n):
    primos = []
    num = 2 
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos
n = int(input("Introduce la cantidad de números primos que deseas mostrar: "))

primos = primeros_n_primos(n)
print(f"Los primeros {n} números primos son: {primos}")