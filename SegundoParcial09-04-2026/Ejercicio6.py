# 1. Texto inicial
texto = "Alex"

# 2. Normalización fuerte
texto_normalizado = texto.casefold()

# 3. Verificar si contiene solo letras (sin espacios)
texto_sin_espacios = texto_normalizado.replace(" ", "")
es_alfabetico = texto_sin_espacios.isalpha()

# Mostrar resultados
print("Texto normalizado:", texto_normalizado)
print("¿Solo letras?:", es_alfabetico)
