def transformar_texto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


texto = input("Ingrese un texto: ")
numero = int(input("Ingrese una opción (1,2,3): "))

print(transformar_texto(texto, numero))
