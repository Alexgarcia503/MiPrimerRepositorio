def transformar_lista(lista, numero):
    resultado = []

    for palabra in lista:
        if numero == 1:
            resultado.append(palabra.upper())
        elif numero == 2:
            resultado.append(palabra.lower())
        elif numero == 3:
            resultado.append(palabra.capitalize())
        else:
            return "Opción inválida"

    return resultado


lista = ["hola", "MUNDO", "Python"]
print(transformar_lista(lista, 1))
