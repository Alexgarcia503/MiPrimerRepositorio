Algoritmo Ejercicio01Parcial
	
	Definir nota1 Como Entero
	
	Escribir "Ingrese la nota de un estudiante del 1 al 10"
	Leer nota1
	
	
	Repetir 
	Si nota1 < 0 O nota1 > 10 Entonces
		Escribir "Error, la nota debe ser entre 0 al 10"
		Escribir "Ingrese una nota del 1 al 10"
		leer nota1
	Finsi
	Hasta que nota1 >= 0 Y nota1 <= 10
	


	Si nota1 >= 6  Entonces
		Escribir "Aprobado"
	FinSi
	 Si nota1 == 5 Entonces
		 Escribir "Recuperacion"
	 FinSi

	Si nota1 <= 4 Entonces
			Escribir "Reprobado"
	FinSi
	
FinAlgoritmo
