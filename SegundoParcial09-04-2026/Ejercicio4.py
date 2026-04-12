# 1. Palabra inicial
texto = "CANTANDO"

# 2. Convertir a minúsculas
texto_minusculas = texto.lower()

# 3. Eliminar el sufijo correctamente
texto_sin_sufijo = texto_minusculas.removesuffix("ando")

# 4. Encontrar el índice de la letra "t"
indice_t = texto_sin_sufijo.find("t")

print("Texto final:", texto_sin_sufijo)
print("Índice de 't':", indice_t)
