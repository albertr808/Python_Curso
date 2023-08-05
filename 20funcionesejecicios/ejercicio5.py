"""programa que valide si la contraseña es segura
    tenga más de 8 caracteres
    tiene al menos una mayuscula
    tiene al menos un numero
"""

# print(len("hola"))
# print("a".isupper())
# print("a".isnumeric())

# cadena = input("ingresa cadena")

# for charcontador in range(len(cadena)):
#     print(charcontador)

# if charcontador < 8:
#     print("ingrese contraseña más larga")


def comprobar(password):
    largo = False
    mayus = False
    numero = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numero = True
    if largo and mayus and numero:
        return True
    else:
        return False
    
contraseña = input("ingresa contraseña")
verificacion = comprobar(contraseña)
if verificacion:
    print("contraseña segura")
else:
    print("contraseña insegura")
