import math

salir = " "
while salir != "no" :
    print("""bienvenido a la calculadora, pra ingresar la operacion ingrese la palabra:
            \"sum\" \"rest\" \"multi\" \"div\
            para salir ingresa\"salir\" """)
    operacion = input("ingrese la operacion")
    numero = int(input("ingrese un numero"))
    numero2 = int(input("ingrese otro numero "))
    if operacion == "sum":
        suma = numero + numero2
        print(suma)
    elif operacion == "rest":
        resta = numero - numero2
        print(resta)
    elif operacion == "multi":
        multi = numero * numero2
        print(multi)
    elif operacion == "div":
        div = numero/numero2
        print(div) 
    salir = input("desea hacer otra operacion? ")
print("adios :) ")
