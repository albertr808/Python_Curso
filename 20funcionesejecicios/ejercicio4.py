def tablamultiplicar(numero):
    tabla = []
    for i in range(11):
        resultado = numero * i
        tabla.append(resultado)
    return tabla

numero = int(input("ingrese un numero"))
resultado_tabla2= tablamultiplicar(numero)
print(resultado_tabla2[10])
