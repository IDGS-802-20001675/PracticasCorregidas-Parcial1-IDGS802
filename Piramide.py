'''
Práctica 2 "Pirámide" Vanessa Fernández Solís 18/01/2024
'''
def piramide():
    
    #Pedir la cantidad de números para 
    numeros = int(input("Ingrese la cantidad de números para la pirámide: "))

    while numeros <= 0:
        #Restricción para que no ponga un valor de 0
        print("Se debe ingresar un número mayor a 0")
        numeros = int(input("¿Cuántos números quiere que tenga la pirámide? "))

    for i in range(1, numeros + 1):
        # Utilizo concatenación de cadenas para imprimir pirámide
        asteriscos = "*" * i
        print(asteriscos)

# Llamar a la función
piramide()

