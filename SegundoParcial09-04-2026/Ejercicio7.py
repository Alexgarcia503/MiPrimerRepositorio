# 1. Texto numérico
texto = "42"

# 2. Rellenar con ceros a la izquierda hasta 5 caracteres
texto_rellenado = texto.zfill(5)

# 3. Verificar si termina en "2"
termina_en_2 = texto_rellenado.endswith("2")

# Mostrar resultados
print("Texto rellenado:", texto_rellenado)
print("¿Termina en '2'?:", termina_en_2)
