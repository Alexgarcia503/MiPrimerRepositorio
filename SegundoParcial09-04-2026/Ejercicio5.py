# 1. Cadena inicial
texto = "pYTHON"

# 2. Invertir mayúsculas y minúsculas
texto_invertido = texto.swapcase()

# 3. Alinear a la izquierda en 15 caracteres, rellenando con "*"
texto_final = texto_invertido.ljust(15, "*")

# Mostrar resultado
print("Texto final:", texto_final)
