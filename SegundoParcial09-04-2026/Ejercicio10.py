# 1. Cadena inicial
texto = "Python2026"

# 2. Verificar si es alfanumérico
es_alfanumerico = texto.isalnum()

# 3. Si es alfanumérico, transformar y separar
if es_alfanumerico:
    texto_minusculas = texto.lower()
    palabra = texto_minusculas.replace("2026", "")
else:
    palabra = "No es alfanumérico"

# Mostrar resultados
print("¿Es alfanumérico?:", es_alfanumerico)
print("Texto separado:", palabra)
