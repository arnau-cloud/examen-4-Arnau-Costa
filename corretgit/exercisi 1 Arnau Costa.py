any = input("Quin any vas nèixer entre el 2010 i el 2013: ")

match any:
    case 2010:
        print("Estas fent 4t d'eso")
    case 2011:
        print("Estas fent 3r d'eso")
    case 2012:
        print("Estas fent 2n d'eso")
    case 2013:
        print("Estas fent 1r d'eso")
    case _:
        print("Incorrecte")