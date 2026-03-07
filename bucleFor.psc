Funcion respuesta <- validar ( usuario, pass ) 
	respuesta = Falso
	Escribir "validar usuario"
	
	Si usuario == "AlexCarballo"  Entonces
		Si pass == "alex" Entonces
			Escribir "Bienvenido"
		SiNo
			Escribir "fallo de contraseña"
		Fin Si
	SiNo
		Escribir "fallo de usuario"
	Fin Si
FinFuncion
// funcion
// encapsulacion -> siempre ve a dar la misma salida
// va a crear algo que se llama scope


// las variables siempre tiene que tener sentido
// edad = 32 funcion entero <- registrarpersona(edad)
//funcion entero <- registrarpersona(xw)
//nombre en clave de las variables nombre de ex, nombre de personajes, fechas....
//	xw = "Hola como estas"
//	nomeclatura camelCase snekCase
Algoritmo bucleFor
	//indica que vamos a repetir los pasos o un algoritmo en un numero de pasos
	
	//yo quiero utilizar la cuenta de correo
	//pero si me equivoco mas de 4 veces
	// se bloquea momentaneamente
	
	
	Escribir "registrar usuario"
	leer usuario
	
	Escribir "registrar PASS"
	leer pass
	
	Definir i Como Entero
	resultado = validar ( usuario , pass) 
	Para i <- 1 Hasta 5 Con Paso 1 Hacer
		si resultado == Verdadero
			Escribir "Bienvenida"
			Escribir "Indicaciones"
		FinSi
		resultado = false
	FinPara
	
	// for i = 0 ; instruccionLogica i> 20 ;
	// i = i + 1 ....19 detener el bucle
	
	
	
	//funcion es una estrucutra de codigo
	//que se puede repetir pero siempre se llama a la misma isntancia
	//bajo el mismo nombre
	
	//palabra re.	si nos devuelve algo 	()
	//argumentos: son las entradas de las funciones van entre parentesis y puede ser
	//mas de una o ninguna
	// caracteristicas -> el carro es rojo
	//						nosotros somos feos
	//					edad				32
	//					boolean			verdad o Flaso
	//					objeto: un objeto es aquella entidad
	
	
	
	
FinAlgoritmo
