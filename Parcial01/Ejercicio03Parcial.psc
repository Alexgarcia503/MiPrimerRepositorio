Algoritmo Ejercicio03Parcial
	
	Definir numero1 Como Entero
	
	Escribir "Ingrese un numero del 1 al 7"
	leer numero1
	
	Segun numero1 Hacer
		
		1:
			Escribir "Lunes"
		2:
			Escribir "Martes"
		3:
			Escribir "Miercoles"
		4:
			Escribir "Jueves"
		5:
			Escribir "Viernes"
		6:
			Escribir "Sabado"
		7:
			Escribir "Domingo"
			
		De Otro Modo:
			Si numero1 < 0 O numero1 > 7 Entonces
				Escribir "El numero no puede ser mayor de 7 ni menor de 1"
			FinSi
	FinSegun
	
FinAlgoritmo
