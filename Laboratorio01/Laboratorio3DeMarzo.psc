Algoritmo RestarHasta0Laboratorio
	Definir valor1, respuesta Como entero
	
	Escribir "Ingrese un número inicial"
	Leer valor1

	
	respuesta = valor1 
	
	Repetir
		Leer valor1
		respuesta = respuesta - valor1
		Escribir "El resultado es " , respuesta

	Hasta Que (respuesta = 0 O respuesta < 0) = Verdadero
		
FinAlgoritmo
	

