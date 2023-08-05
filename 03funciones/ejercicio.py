def no_space(texto):
    nuevotexto = ""
    for char in texto:
        if char != " ":
            nuevotexto = nuevotexto + char
    return nuevotexto

def es_palindromo(texto):
    texto = no_space(texto)
    print(texto)
    if texto[::-1] == texto:
        print("es palindromo")
    else:
        print("no lo es")
es_palindromo("somos o no somos")