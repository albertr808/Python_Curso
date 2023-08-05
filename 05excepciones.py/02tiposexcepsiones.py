# try:
#     n1 = int(input("ingresa un numero"))
# except Exception as e:
#     print(type(e))

try:
    n1 = int(input("ingresa un numero"))
    # ASDF
except ValueError as e:
    print("INGRESE UN VALOR QUE CORRESPONDA")
except NameError as e:
    print("ocurrio un error")