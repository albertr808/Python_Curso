numero = 1

while numero < 11:  
    print(numero)  
    numero +=1

##palabra secreta
contraseña = "" #hola
while contraseña != "12345":
    contraseña = input("ingrese la contraseña")
    if contraseña == "salir":
        break