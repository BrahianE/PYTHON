"""Ejercico 3 a 
Escriba un programa que reciba una cantidad de numeros y devuelva el mayor 
""" 
def obtener_numeros():
    numeros = []
    while true:
        entrada = input("ingrese un numero (o 'q' para salir): ")
        if entrada.lower()== 'q':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except valueError:
            print("por favor, ingrese un numero valido.") 
            return numeros
        lista = obtener_numeros
        print(lista)  
        print("mayor:") (lista) 
        print("mayor:") (lista)

              