frutas = {"platano":1.35,
          "manzana":0.80,
          "pera":0.80,
          "naranja":0.70}

fruta = input("ingrese su fruta")
kilos = int(input("ingrese los kilos"))
if fruta in frutas:
    print(f"son {frutas[fruta]*kilos}$ ")
else:
    print("no existe")