import random

# Crear una lista con 13 números aleatorios entre 1 y 99
lista_aleatoria = [random.randint(1, 99) for _ in range(13)]

# Crear listas para pares, impares y números divisibles por 3
lista_pares = []
lista_impares = []
lista_divisible_por_3 = []

# Separar los números en las listas correspondientes
for numero in lista_aleatoria:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    if numero % 3 == 0:
        lista_divisible_por_3.append(numero)

# Calcular promedios (utilizando sum() y len() para mayor eficiencia)
promedio_aleatoria = sum(lista_aleatoria) / len(lista_aleatoria)
promedio_pares = sum(lista_pares) / len(lista_pares) if lista_pares else 0  # Evitar división por cero
promedio_impares = sum(lista_impares) / len(lista_impares) if lista_impares else 0
promedio_divisible_por_3 = sum(lista_divisible_por_3) / len(lista_divisible_por_3) if lista_divisible_por_3 else 0

# Mostrar resultados
print("Tamaño de la lista aleatoria:", len(lista_aleatoria))
print("Lista aleatoria:", lista_aleatoria)
print("Tamaño de la lista de pares:", len(lista_pares))
print("Lista de pares:", lista_pares)
print("Tamaño de la lista de impares:", len(lista_impares))
print("Lista de impares:", lista_impares)
print("Tamaño de la lista de números divisibles por 3:", len(lista_divisible_por_3))
print("Lista de números divisibles por 3:", lista_divisible_por_3)

print("\nLista aleatoria ordenada:", sorted(lista_aleatoria))
print("Lista de pares ordenada:", sorted(lista_pares))
print("Lista de impares ordenada:", sorted(lista_impares))
print("Lista de números divisibles por 3 ordenada:", sorted(lista_divisible_por_3))

print("\nPromedio de la lista aleatoria:", promedio_aleatoria)
print("Promedio de la lista de pares:", promedio_pares)
print("Promedio de la lista de impares:", promedio_impares)
print("Promedio de la lista de números divisibles por 3:", promedio_divisible_por_3)