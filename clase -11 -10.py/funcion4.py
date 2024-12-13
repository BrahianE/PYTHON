""""
funciones con argumentos variables 
""""
def varios (*var):
    for i in var:
    print(f"{i}")

varios(1)
varios(1,"dos")
varios(3,4,5)
varios("uno , "dos , "tres", "cuatro")

def fun_c_v(**cv):
    for c,v in cv,items():
        print(f"clave: {c}, valor: {v}")
        
fun_c_v(clave1="valor1" ,clave2="valor2")
fun_c_v(nombre="ana", apellidos="balbuena", edada=23)

def login(**cred):
    for c,v in cred.items():
    if c== "celular":
       print(f"login por celular: {v}")
    elif c == "email":
    )  print()      