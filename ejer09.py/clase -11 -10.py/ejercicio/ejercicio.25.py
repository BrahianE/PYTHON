""" Ejercicio 01
escribir un programa que pida dos numeros y me de la suma, la resta, la multiplicacion, la division y modulo por eleccion por teclado
"""
var1=float(input("escriba un nro"))
var2=float(input("escriba un nro"))

suma = var1 + var2
print(f"la suma es: {suma}")
r= var1 * var2
print(f"la resta es: {r}")
multip= var1 * var2
print(f"la multiplicacion es: {multip}")
d= var1 / var2 if var2 != 0 else 0
print(f"la division es: {d:.2f}")
modulo= var1% var2 if var2 !=0 else 0
print(f"el modulo es: {modulo}")
