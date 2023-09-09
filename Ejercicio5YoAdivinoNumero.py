import random

numero_oculto = random.randint(1, 100)
intentos = 0

print("Adivina el número")

while True:
    intentos += 1
    print(f"Intento: {intentos}")

    try:
        numero_jugador = int(input("Ingresa un número: "))
    except ValueError:
        print("¡Ingresa un número válido!")
        continue

    if numero_jugador > numero_oculto:
        print(f"El número es menor que {numero_jugador}")
    elif numero_jugador < numero_oculto:
        print(f"El número es mayor que {numero_jugador}")
    else:
        print(f"Bien adivinaste el número en {intentos} intentos.")
        break
