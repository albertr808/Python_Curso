import math
#programa que tome las tres notas de un estudiantes y diga la nota final del curso.
#la primta y segunda nota valen el 30% de la nota final, la tercera vale el 40%.

#nota 1 = 30%
#nota 2 = 30 %
#nota 3 = 40%
#nota final = nota1+nota+nota3 / 3

#porcenaje  calif*100/100

def calf_final(n1,n2,n3):

    n1 = (n1*30)/100
    n2 = (n2*30)/100
    n3 = (n3*40)/100
    return n1+n2+n3


calificacion1 =  calf_final(4.4,4,4.6)
print(round(calificacion1))