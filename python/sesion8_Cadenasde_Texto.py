# la comillas triples son las que permiten escribir en varias lineas

# Textos Largos
poema = """La noche está estrellada,
y tiritan, azules, los astros, a lo lejos".
El viento de la noche gira en el cielo y canta.
Puedo escribir los versos más tristes esta noche.
Yo la quise, y a veces ella también me quiso.
En las noches como ésta la tuve entre mis brazos.
La besé tantas veces bajo el cielo infinito.
Ella me quiso, a veces yo también la quería.
Cómo no haber amado sus grandes ojos fijos.
Puedo escribir los versos más tristes esta noche.
Pensar que no la tengo. Sentir que la he perdido.
Oír la noche inmensa, más inmensa sin ella.
Y el verso cae al alma como al pasto el rocío.
Qué importa que mi amor no pudiera guardarla.
La noche está estrellada y ella no está conmigo."""

## print(poema)

## computadora -> que variable queres imprimir
## print() =>
# void -> no devuelve nada
# objeto -> devuelve un tipo de dato

## realizar una wiki tambien puede darle doble click documento y
## se les despliega el editor de texto

## MAYUSCULAS
## multabilidad -> siempre debemos evitar tansformar objeto original
## clases -> estereotipo (como un molde)
## propiedades ->
## color
# tipo de motor ( electricos o de gas)
# Ojos
# color de pelo

# moverse
# frenar
# cargarse
# descargarse

# poema es un espacio de memoria para string
# se va llenar el contenido de poema alterar con al accion Upper
## poema_Mayusculas = poema.upper()
## print(poema_Mayusculas)

# convertir en minusculas
## string .lower

poema_minuscula = poema.lower()
print(poema_minuscula)

## tiene que ingresar 100 nombrs en mayuscula
mensaje = "hola kace progrmando o ke hace"
## Capitalize a que la primera letra de cada palabra sea mayuscula
mensajeCorrecto = mensaje.capitalize()
print(mensajeCorrecto)

## las fliapntes aventuras de el gato
titulo = "Las flipantes aventuras de el gato con bolson magico y alfredo"
tituloCorrecto = titulo.title()
print(tituloCorrecto)

# swapcase permite camboar el orden entre mayusculas y minusculas
swapCaseTitulo = tituloCorrecto.swapcase()
print(swapCaseTitulo)

## metodos de validacion
# false numeros o espacio
# true tiene solo letras

numero = "512"
solo_letras = "El chico del apartamentos"
Coro = "piribiri_ban_ban"

quieroSololetras = numero.isalpha()
print(quieroSololetras)
