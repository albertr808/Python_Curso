def get_product(**datos):
    print(datos)
    print(datos["id"],datos["nombre"],datos["precio"])

get_product(id="01",nombre="iphone",desc="esto es un iphone",precio=15000)