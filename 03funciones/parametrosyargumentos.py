def  hola(nombre,apellido="...",apellido2="..."): # (nombre)parametro,-podemos tener parametros opcionales

    print(f"bienvenido {nombre} {apellido} {apellido2}") #{nombre} es un parametro

    
hola("Alberto","Ramirez","baltazar") #("alberto") es un argumento 
hola("Alberto") 
#podemos nombrar los argumentos
hola(apellido="baltazar",apellido2="ramirez",nombre="albertooooo")