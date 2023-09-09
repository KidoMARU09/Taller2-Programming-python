numero = int(input("¿Cuantos datos ingresará?\nRespuesta: "))
vector_de_rangos = []

for i in range(numero):
    valor = float(input(f"Valor {i + 1}: "))
    vector_de_rangos.append(valor)

mayor = vector_de_rangos[0]
menor = vector_de_rangos[0]

for valor in vector_de_rangos:
    if valor > mayor:
        mayor = valor
    if valor < menor:
        menor = valor

rango = mayor - menor
print(f"El rango es de {rango}")