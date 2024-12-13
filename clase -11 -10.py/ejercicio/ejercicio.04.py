"""Funciones sobre cadenas"""

cad = input("introduzca una cadena:")
mayus = cad.upper()
minus = cad.lower()
print(mayus)
print(minus)
cap = cad.capitalize()
print(cap)

if cad.islower():
    print("esta en minuscula")
elif cad.isupper():
    print("esta en mayuscula") 
elif cad.istitle():
    print("esta en capital") 
else:
    print("es otro")          
    