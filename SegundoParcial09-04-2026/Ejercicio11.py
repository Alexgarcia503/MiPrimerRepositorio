# 1. Cadena inicial
texto = "  el nido matinal  "

# 2. Limpiar espacios y convertir a formato título
texto_procesado = texto.strip().title()

# 3. Centrar en 30 caracteres con "-"
texto_final = texto_procesado.center(30, "-")

# Mostrar resultado
print("Texto final:", texto_final)
