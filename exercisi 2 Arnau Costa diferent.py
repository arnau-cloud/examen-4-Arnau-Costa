import re

def comprovar(any):
    if any % 4 == 0:
        return any

anysTraspas = list()

while True:
    any = input("Introdueix dos anys separats per un espai: ")
    anysepar = re.split("\\s", any)
    if len(anysepar) <  2:
        print("incorrecte")
    else: break

a = int(anysepar[0])
b = int(anysepar[1])

try:
    for i in list(map(comprovar, range(a, b))):
        if i != None:
            anysTraspas.append(i)

    if len(anysTraspas) > 0:
        print(anysTraspas)
    else:
        print("No hi ha anys de traspàs")
        
    if len(anysTraspas) < 5:
        print("No hi ha prous anys per imprimir el 5è")
    else:
        print(anysTraspas[5])
except:
    print("Incorrecte")