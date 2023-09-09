numeros = []

print("Ingrese números ordenados (ingrese '.' para terminar):")

while True:
    entrada = input()
    if entrada == '.':
        break
    else:
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no válida. Ingrese números enteros o '.' para terminar.")

cantidad_numeros = len(numeros)

if cantidad_numeros % 2 == 1:
    mediana = numeros[cantidad_numeros // 2]
    print("La mediana es:", mediana)
else:
    numero1 = numeros[(cantidad_numeros - 1) // 2]
    numero2 = numeros[cantidad_numeros // 2]
    promedio = (numero1 + numero2) / 2.0
    print("La mediana es:", promedio)
