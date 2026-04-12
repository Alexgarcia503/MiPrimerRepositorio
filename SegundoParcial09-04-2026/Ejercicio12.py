# 1. Nombre de archivo
texto = "Alex.txt"

# 2. Remover sufijo y prefijo
texto_sin_txt = texto.removesuffix(".txt")
texto_limpio = texto_sin_txt.removeprefix("ING. ")

# 3. Convertir a minúsculas
texto_final = texto_limpio.lower()

# Mostrar resultado
print("Texto final:", texto_final)
