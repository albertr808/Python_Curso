class MiError(Exception): #como parametro podemos pasarle cualquier excepcion
#si no sabemo especificamente el error, ponemos solo Excepcion
    "esta clase es para representar mi error"
    def __init__(self,mensaje,codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    def __str__(self):
        return f"{self.mensaje} - codigo {self.codigo}"

def division(n=0):
    if n == 0:
        raise MiError("no se puede dividir entre cero",805)#hay que ser especificos al invocar una excepción
    return 5/n

try:
    division()
except MiError as e:
    print(e)

    #las excepciciones consumen mucho rendimiento