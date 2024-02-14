num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
option = int(input("ingrese 1 si quiere sumar los numeros, ingrese 2 si los quiere restar"))


def sumar(a, b, option):
    if(option == 1):
        return a + b
    if(option == 2):
        return a - b
    else:
        print("opcion equivocada")
        

print(sumar(num1, num2, option))