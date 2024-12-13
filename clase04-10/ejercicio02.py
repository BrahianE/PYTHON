"""
Concatenar Cadenas
"""
print(__doc__)
print(__doc__) # inprimir documentacion

cadena1 = "Hola"
cadena2 = "Mundo"

concat = cadena1 + cadena2
concat2 = cadena1 + " " + cadena2

print(concat)
print(concat2)
print(cadena1,cadena2,concat,concat2)

nro = 3
#cade = cadena1 + nro
print(type(nro))
print(type(cadena1))
#print(type(cade))
print(type(2.5))
‎Clase_04-10/ejer03.py
+7
-7
Original file line number	Diff line number	Diff line change
@@ -12,10 +12,10 @@
""" for i in cadena:
    print(i) """

print(cadena[0])
print(cadena[1:4])
print(cadena[::-1])
print(cadena[:4])
print(cadena[7:])
print(cadena[-4:])
print(cadena[-4::-1])
print(cadena[0]) # primera letra
print(cadena[1:4]) # desde la segunda hasta la cuarta
print(cadena[::-1]) # invertir
print(cadena[:4]) # desde la primera hasta la cuarta
print(cadena[7:]) # desde la octava
print(cadena[-4:]) # desde la cuarta invertido
print(cadena[-4::-1]) # desde la cuarta invertido