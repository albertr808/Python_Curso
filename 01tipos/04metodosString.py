fruta = "manzana verde"
fruta2 = "      manzana roja     "

print(fruta.upper())        #convierte todo a letras mayusculas
print(fruta.lower());        #convierte todo a minusculas
print(fruta.capitalize());   #convierte el primer caracter del string en Mayuscula
print(fruta.title());        #toma la primera letra de cada palabra y la pasa a mayuscula.
print(fruta2.strip());       #remueve todos los espacios que se er4encuentra a la dereche e izquierda
print(fruta2.strip().capitalize())
print(fruta2.rstrip());      #remueve los espacios de la derecha
print(fruta2.lstrip());      #remueve los espacios de la izquierda
print(fruta.find("nz"));     #busca el caracter indica y muestra su indice
print(fruta.replace("verde","amarilla")) #remplaza los caracteres
print("nz" in fruta);        #muestra si el caracter o cdna de caracteres existe o no en la cadena
