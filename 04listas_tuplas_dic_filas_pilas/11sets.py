# set significa conjunto o grupo
#coleccion de datos que no se repite y no esta ordenada

primerSet = {1,2,3,4,4,4}

print(primerSet) #los sets se trabajan igual que las listas
primerSet.add(5)
primerSet.remove(1)
print(primerSet)

#transformar lista a set

segundo = [8,9,10,2]
segundo = set(segundo)
print("unir,int,dif,difsimetrica")
print(segundo)
print(primerSet | segundo)  #podemos unir sets con  "|"
print(primerSet & segundo)  #interseccion "&"
print(segundo - primerSet) #diferencia con el primer set
print(primerSet ^ segundo) #diferencia simetrica

if 2 in segundo:
    print("existe")