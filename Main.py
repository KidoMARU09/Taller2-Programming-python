positivo = 0
negativo = 0
numero = None

print("Ingrese números enteros y termine con cero.")
while True:
    numero = int(input())
    if numero <= -1:
        negativo += 1
    else:
        positivo += 1
    if numero == 0:
        break

print("Positivos: " + "*" * positivo)
print("Negativos: " + "*" * negativo)