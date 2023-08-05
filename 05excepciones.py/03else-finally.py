try:
    n1 = int(input("ingresa un numero"))
except Exception as e:
    print("ocurrio un error")
else:
    print("no ocurrio ningun error")
finally:
    print("se ejecuta siempre")
#finally se utiliza independiente de si va o no va a tener exito
#y else si se va a agregar una siguiente ejecucion de codigo y no haya ningun error