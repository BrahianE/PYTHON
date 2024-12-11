lista = ["ana" , "eduardo", "luis", "juan" , "pedro","briam", "john"]
def saludar(x="mundo"):
    print(f"hola, [x]!")



saludar()
for i in lista:
    saludar(i)
    
for i in tupla:
    saludar(i)
    
for i in sets:
    saludar(i)        
    
    
    def sal(x):
        return f"hola,{x}!"
    
    s = [sal(i) for i in lista]
    # print(s)
    
    for i in s:
        print(i)