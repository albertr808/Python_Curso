"""programa que calcule la tabal de multiplicar de cualquier numero dado por el usuario
del 0 hasta el 12"""

def multiplicar (n1,n2):
    return f"{n1} * {n2} = {n1*n2}"

def multi():
    n = int(input("ingrese un numero"))
    for i in range(13):
        print (multiplicar(i,n))


tb2 = multi()
print(tb2)