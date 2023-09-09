numero = input("Ingrese un número: ")

if numero == numero[::-1]:
    print(f"El número {numero} es palíndromo.")
else:
    print(f"El número {numero} no es palíndromo.")
