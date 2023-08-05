def suma(a,b,c):
    print(a+b+c)

suma(2,5,3)

def suma2(*numeros): #agregamos el ast para saber que va hacer algo iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma2(1,2,3,4,5)

#############################################
resultado2 = 0
for numeros2 in range(1,6):
    resultado2 = resultado2 + numeros2
print(resultado2)