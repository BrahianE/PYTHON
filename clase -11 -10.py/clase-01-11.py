"""
Ejercicio 01
Escribir un programa que pida al usuario adivinar un numero entre 1 y 100
"""
import random

def rand():

       # genera un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
intentos = 0

print("bienvenido al juego de adivinanzas!")
print("estoy pensando en un numero entre 1 y 100,")

while True:
    
    suposicion = int(input("adivina el numero:"))
    intentos += 1
    
    # compara la suposicion con el numero secreto
    if suposicion < numero_secreto:
        print("demasiado bajo")
    elif suposicion > numero_secreto:
        print("demasiado alto")
    else:
        print(f"correcto lo adivinaste en (intentos) intentos.")
        break
    
    if__name__== "__main__": 
       while True:
            rand()
            op = int(input("0 - continuar jugando.\n1 - salir\n-")
                     if op != 0:
                         break)
        