Algoritmo Ejercicio10Parcial
	
	Definir valor1, valor2 Como Entero
	
	Escribir "Ingrese el primer numero"
	leer valor1
	
	Escribir "Ingrese el segundo numero"
	leer valor2
	
	Si valor1 > valor2 Entonces
		Escribir "El numero mayor es ", valor1
		Escribir "El numero menor es ", valor2
	SiNo
		Si valor2 > valor1 Entonces
			Escribir "El numero mayor es ", valor2
			Escribir "El numero menor es ", valor1
		SiNo
			Escribir "Ambos numeros son iguales"
		FinSi
	FinSi
FinAlgoritmo
