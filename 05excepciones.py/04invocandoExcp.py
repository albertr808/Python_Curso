def division(n=0):
    if n == 0:
        raise ZeroDivisionError("no se puede dividir entre cero")#hay que ser especificos al invocar una excepción
    return 5/n

try:
    division()
except ZeroDivisionError as e:
    print(e)

    #las excepciciones consumen mucho rendimiento