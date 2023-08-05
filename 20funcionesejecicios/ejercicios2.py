#programa que calcule el iva de una compra , siendo el iva del 19% sobre el valor de la compra

def calcularIva(precio):
    precioFinal = precio * 1.19

    return precioFinal

producto1 = calcularIva(10)
print(producto1)