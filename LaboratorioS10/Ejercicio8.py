def transformar_texto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


while True:
    print("\n--- MENÚ ---")
    print("1. Mayúsculas")
    print("2. Minúsculas")
    print("3. Capitalizar")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 4:
        break

    texto = input("Ingrese un texto: ")
    print(transformar_texto(texto, opcion))