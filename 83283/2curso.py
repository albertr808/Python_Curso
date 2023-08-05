my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    print("no hay cambios")
    for i in range(len(my_list) - 1):  #itera 4 veces
        if my_list[i] > my_list[i + 1]: #
            swapped = True  # ¡ocurrió el intercambio!
            print("ocurrio un cambio")
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            print(my_list)