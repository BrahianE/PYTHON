def analizar_cadena(cadena):
    """
    Analiza una cadena de texto y devuelve un diccionario con los resultados.

    Args:
        cadena (str): La cadena de texto a analizar.

    Returns:
        dict: Un diccionario con los siguientes elementos:
            - vocales: Cantidad de vocales.
            - consonantes: Cantidad de consonantes.
            - otros: Cantidad de otros caracteres.
            - palabras: Cantidad de palabras.
            - tiene_que: True si la palabra "que" está presente, False en caso contrario.
            - mayusculas: Cantidad de mayúsculas.
            - minusculas: Cantidad de minúsculas.
            - a: Cantidad de letras "a".
            - f: Cantidad de letras "f".
    """

    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnñpqrstvwxyz"

    resultados = {
        "vocales": 0,
        "consonantes": 0,
        "otros": 0,
        "palabras": 0,
        "tiene_que": False,
        "mayusculas": 0,
        "minusculas": 0,
        "a": 0,
        "f": 0
    }

    palabras = cadena.split()
    resultados["palabras"] = len(palabras)
    resultados["tiene_que"] = "que" in palabras

    for caracter in cadena:
        if caracter.lower() in vocales:
            resultados["vocales"] += 1
        elif caracter.lower() in consonantes:
            resultados["consonantes"] += 1
        else:
            resultados["otros"] += 1

        if caracter.isupper():
            resultados["mayusculas"] += 1
        elif caracter.islower():
            resultados["minusculas"] += 1

        if caracter.lower() == "a":
            resultados["a"] += 1
        elif caracter.lower() == "f":
            resultados["f"] += 1

    return resultados

# Solicitar la cadena al usuario
cadena = input("Ingrese una cadena de texto: ")

# Analizar la cadena y mostrar los resultados
resultados = analizar_cadena(cadena)
print(resultados)