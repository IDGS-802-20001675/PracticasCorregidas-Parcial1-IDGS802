'''
Práctica 1 "Numeros" Vanessa Fernández Solís 18/01/2024
'''
def p1numeros():
    # Crear la lista de números
    numeros = []

    # El usuario ingresa 10 números con un bucle for
    for i in range(10):
        numero = int(input("Dame el valor del número {}: ".format(i + 1)))
        numeros = numeros + [numero]  # Evitar el uso de append

    # Imprimir la lista de números después de que el usuario haya ingresado todos los valores
    print("\nLos números que ingresaste son: " + str(numeros))

    # Clasificar números pares e impares y ordenar
    pares = []
    impares = []
    ordenados = []

    for num in numeros:
        # Para pares e impares
        pares += [num] if num % 2 == 0 else []
        impares += [num] if num % 2 != 0 else []

        # Para ordenar los numeros
        for i, sorted_num in enumerate(ordenados):
            if num < sorted_num:
                ordenados = ordenados[:i] + [num] + ordenados[i:]
                break
        else:
            ordenados += [num]

    # Utilizar set para que no se repitan pares e impares 
    pares = list(set(pares))
    impares = list(set(impares))

    # Imprimir resultado
    print("\nLos números pares son: " + str(pares))
    print("Los números impares son: " + str(impares))
    print("Los números ordenados son: " + str(ordenados))

# Llamar a la función
p1numeros()

