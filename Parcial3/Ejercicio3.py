temperaturas = []

# Solicitar 5 temperaturas
for i in range(5):
    temp = int(input(f"Ingrese la temperatura #{i + 1}: "))
    temperaturas.append(temp)

# Evaluar temperaturas
for temperatura in temperaturas:

    match temperatura:

        case 0:
            print("Alerta: Punto de Congelación")

        case 100:
            print("Alerta: Punto de Ebullición")

        case _:
            estado = "Estado: Estable" if 10 <= temperatura <= 30 else "Estado: Crítico"

            print(estado)
