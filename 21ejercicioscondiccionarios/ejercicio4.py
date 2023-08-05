datos_usuario = {}

menu = """
1.agregar datos
2.salir"""

while True:
    print(menu)
    opcion = int(input("que quieres hacer"))

    if opcion == 1:
        clave_nueva = input("ingresa una clave nueva")
        valor_nuevo = input("inserta un valor nuevo")
        nuevo = datos_usuario.setdefault(clave_nueva,valor_nuevo)
        print(datos_usuario)
    else:
        break