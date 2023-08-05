nombre = "Alberto" #string normal(no deja escribir mas de una linea de codigo)

descripcion = """HolamundoHolamundoHolamundoHolamundoHolamundo
                HolamundoHolamundoHolamundoHolamundoHolamundo
                HolamundoHolamundoHolamundoHolamundoHolamundo
                """  # comillas tripes(estas nos dejan escribir en  mas de una linea de codigo)
print(nombre)
print (descripcion)

#funciones para string
#len : obtiene la longitud de una string

print(len(descripcion))
print(descripcion[31]) #acceder a un caracter de la cadena
print(descripcion[4:9]) #acceder a caracteres en especifico "indice inicial:caracteres a recortar"
print(descripcion[:186])
print(descripcion[160:])
print(descripcion[::-1]) #pone los caracteres al revez