anysTraspas = list()
def comprovar(any, any2, llista):
    for i in range(any, any2):
        if i % 4 == 0:
            llista.append(i)

   
any = int(input("Introdueix un any: "))
any2 = int(input("Introdueix un altre any que sigui mes gran que el primer: "))
try:  
    if any > any2:
        raise ValueError

    comprovar(any, any2, anysTraspas)

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