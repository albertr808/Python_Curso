variables = {"Euro":"e",
            "Dollar":"$",
            "Yen":"Y"}

pregunta = input("que divisa quiere que se muestre")

if pregunta == "euro":
    print(variables.get("Euro"))
elif pregunta == "dollar":
    print(variables.get("Dollar"))
elif pregunta == "yen":
    print(variables.get("Yen"))
else:
    print("no existe")