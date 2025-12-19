def comprovar(any):
    while True:
        if any % 4 == 0:
            yield any
        any += 1

   
any = int(input("Introdueix un any: "))
try:
    anysTraspasGen = comprovar(any)
    for i in range(0,10):
        print(next(anysTraspasGen), end=", ")
        if i == 9:
            print(next(anysTraspasGen))
except:
    print("Incorrecte")