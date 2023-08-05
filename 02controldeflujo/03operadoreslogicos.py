# and, or y not
#se leen de izquierda a derecha
edad = 61
estatura = 1.80
humano = not True

if edad >= 18 and edad > 1.60:
    print("puede pasar")

if edad > 60 or edad <17:
    print("no pasa")

if humano == True and edad >= 18 and estatura > 1.60:
    print("puede pasar")


if humano and (edad >= 18 or estatura > 1.60):
    print("puede pasar")