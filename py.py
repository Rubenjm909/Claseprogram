suma = 0

for numero in range(2, 2000000):
    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        suma = suma + numero
    else:
        pass

print("La suma de todos los primos es:", suma)