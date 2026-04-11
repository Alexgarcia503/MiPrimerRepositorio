# 1. Declarar la variable con espacios
texto = "  elefante  "

# 2. Eliminar espacios en blanco a ambos extremos
texto_limpio = texto.strip()

# 3. Contar cuántas veces se repite la letra "e"
cantidad_e = texto_limpio.count("e")

# Mostrar resultados
print("Texto limpio:", texto_limpio)
print("Cantidad de 'e':", cantidad_e)
