Algoritmo Sistema_Tortilleria
	Definir usuario, respuesta, opcion Como Cadena
	Definir opcionProducto, nombreProducto Como Cadena
	Definir contenido, documento Como Cadena
	Definir dia, mes, anio, caja Como Entero
	Definir minuto, i, cantidad, seleccion Como Entero
	Definir cantidadTickets Como Entero
	Definir dineroGanado, total, subtotal Como Real
	Definir precioTortilla, precioArroz Como Real
	Definir precioSalsa, precioFrijoles Como Real
	Definir kilos Como Real
	Definir inventarioArroz, inventarioSalsa Como Entero
	Definir inventarioFrijoles Como Entero
	Definir ventasTortilla, ventasArroz Como Real
	Definir ventasSalsa, ventasFrijoles Como Real
	Definir salir, regresarInicio, continuar Como Lógico
	Definir productoMayor, productoMenor Como Cadena
	Definir mayor, menor Como Real
	precioTortilla <- 27
	precioArroz <- 35
	precioSalsa <- 21
	precioFrijoles <- 40
	inventarioArroz <- 20
	inventarioSalsa <- 15
	inventarioFrijoles <- 25
	cantidadTickets <- 0
	dineroGanado <- 0
	ventasTortilla <- 0
	ventasArroz <- 0
	ventasSalsa <- 0
	ventasFrijoles <- 0
	salir <- Falso
	Mientras salir=Falso Hacer
		regresarInicio <- Falso
		Escribir '======================================'
		Escribir '       SISTEMA DE LA TORTILLERIA'
		Escribir '======================================'
		Repetir
			Escribir 'Ingrese su nombre de usuario:'
			Leer usuario
			Si usuario='' Entonces
				Escribir 'El nombre no puede estar vacio.'
			FinSi
		Hasta Que usuario<>''
		Escribir 'Bienvenido/a ', usuario
		Escribir 'al sistema de la tortilleria.'
		Repetir
			Escribir 'Ingrese el dia:'
			Leer dia
			Escribir 'Ingrese el mes:'
			Leer mes
			Escribir 'Ingrese el anio:'
			Leer anio
			Si dia<1 O dia>31 O mes<1 O mes>12 O anio<1 Entonces
				Escribir 'Fecha incorrecta.'
			FinSi
		Hasta Que dia>=1 Y dia<=31 Y mes>=1 Y mes<=12 Y anio>=1
		Escribir 'Fecha registrada: ', dia, '/', mes, '/', anio
		Escribir 'Preparando documentos:'
		Escribir 'ventas.txt'
		Escribir 'inventario.txt'
		Escribir 'productos.txt'
		Escribir 'procedimientos.txt'
		Escribir 'Documentos preparados.'
		Escribir 'Cargando sistema...'
		Para i<-1 Hasta 3 Hacer
			Escribir 'Cargando...'
		FinPara
		Escribir 'Sistema listo.'
		Repetir
			Escribir 'Ingrese el numero de caja:'
			Leer caja
			Si caja<=0 Entonces
				Escribir 'El numero de caja debe ser mayor a cero.'
			FinSi
		Hasta Que caja>0
		Mientras regresarInicio=Falso Y salir=Falso Hacer
			Escribir ''
			Escribir '======================================'
			Escribir '             MENU PRINCIPAL'
			Escribir '======================================'
			Escribir '1. Iniciar nueva venta'
			Escribir '2. Leer documentos'
			Escribir '3. Agregar informacion a documentos'
			Escribir '4. Crear documentos nuevos'
			Escribir '5. Administrar inventario'
			Escribir '6. Cambiar de usuario'
			Escribir '7. Cerrar caja y salir'
			Escribir 'Seleccione una opcion:'
			Leer opcion
			Si opcion='' Entonces
				Escribir 'No seleccionaste ninguna opcion.'
				Escribir 'Simulando diez minutos de inactividad.'
				Para minuto<-1 Hasta 10 Hacer
					Escribir 'Minuto ', minuto, ' de 10'
				FinPara
				Repetir
					Escribir 'Desea continuar? Escriba si o no:'
					Leer respuesta
				Hasta Que respuesta='si' O respuesta='no'
				Si respuesta='si' Entonces
					Escribir 'Regresando al menu principal.'
				SiNo
					regresarInicio <- Verdadero
				FinSi
			SiNo
				Según opcion Hacer
					'1':
						Escribir '======================================'
						Escribir '              NUEVA VENTA'
						Escribir '======================================'
						Repetir
							Escribir 'Seleccione la cantidad de tortillas:'
							Escribir '1. Medio kilo'
							Escribir '2. Un kilo'
							Escribir '3. Dos kilos'
							Escribir '4. Tres kilos'
							Escribir '5. Cuatro kilos'
							Leer opcionProducto
							Según opcionProducto Hacer
								'1':
									kilos <- 0.5
								'2':
									kilos <- 1
								'3':
									kilos <- 2
								'4':
									kilos <- 3
								'5':
									kilos <- 4
								De Otro Modo:
									kilos <- 0
									Escribir 'Opcion invalida.'
							FinSegún
						Hasta Que kilos>0
						total <- kilos*precioTortilla
						ventasTortilla <- ventasTortilla+kilos
						continuar <- Verdadero
						Mientras continuar=Verdadero Hacer
							Escribir 'Desea agregar otro producto?'
							Escribir '1. Arroz'
							Escribir '2. Salsa'
							Escribir '3. Frijoles'
							Escribir '4. Terminar compra'
							Leer opcionProducto
							Si opcionProducto='4' Entonces
								continuar <- Falso
							SiNo
								Según opcionProducto Hacer
									'1':
										nombreProducto <- 'Arroz'
										precio <- precioArroz
										seleccion <- 1
									'2':
										nombreProducto <- 'Salsa'
										precio <- precioSalsa
										seleccion <- 2
									'3':
										nombreProducto <- 'Frijoles'
										precio <- precioFrijoles
										seleccion <- 3
									De Otro Modo:
										nombreProducto <- ''
										Escribir 'Opcion invalida.'
								FinSegún
								Si nombreProducto<>'' Entonces
									Escribir 'Cantidad de ', nombreProducto, ' en piezas:'
									Leer cantidad
									Si cantidad<=0 Entonces
										Escribir 'La cantidad debe ser mayor a cero.'
									SiNo
										Si seleccion=1 Entonces
											Si cantidad<=inventarioArroz Entonces
												inventarioArroz <- inventarioArroz-cantidad
												subtotal <- cantidad*precio
												total <- total+subtotal
												ventasArroz <- ventasArroz+cantidad
											SiNo
												Escribir 'Inventario insuficiente.'
											FinSi
										FinSi
										Si seleccion=2 Entonces
											Si cantidad<=inventarioSalsa Entonces
												inventarioSalsa <- inventarioSalsa-cantidad
												subtotal <- cantidad*precio
												total <- total+subtotal
												ventasSalsa <- ventasSalsa+cantidad
											SiNo
												Escribir 'Inventario insuficiente.'
											FinSi
										FinSi
										Si seleccion=3 Entonces
											Si cantidad<=inventarioFrijoles Entonces
												inventarioFrijoles <- inventarioFrijoles-cantidad
												subtotal <- cantidad*precio
												total <- total+subtotal
												ventasFrijoles <- ventasFrijoles+cantidad
											SiNo
												Escribir 'Inventario insuficiente.'
											FinSi
										FinSi
									FinSi
								FinSi
							FinSi
						FinMientras
						Escribir '======================================'
						Escribir '                 TICKET'
						Escribir '======================================'
						Escribir 'Usuario: ', usuario
						Escribir 'Caja: ', caja
						Escribir 'Fecha: ', dia, '/', mes, '/', anio
						Escribir 'Tortillas: ', kilos, ' kg'
						Escribir 'TOTAL: $', total
						cantidadTickets <- cantidadTickets+1
						dineroGanado <- dineroGanado+total
						Escribir 'Venta registrada.'
						Escribir 'Inventario actualizado.'
						Escribir 'Registro de venta agregado a ventas.txt.'
					'2':
						Escribir 'DOCUMENTOS DISPONIBLES'
						Escribir '1. ventas.txt'
						Escribir '2. inventario.txt'
						Escribir '3. productos.txt'
						Escribir '4. procedimientos.txt'
						Escribir 'Seleccione el documento:'
						Leer seleccion
						Según seleccion Hacer
							1:
								Escribir 'Mostrando historial de ventas.'
							2:
								Escribir 'Mostrando inventario.'
								Escribir 'Arroz: ', inventarioArroz
								Escribir 'Salsa: ', inventarioSalsa
								Escribir 'Frijoles: ', inventarioFrijoles
							3:
								Escribir 'Tortilla: $27 por kilogramo.'
								Escribir 'Arroz: $35 por pieza.'
								Escribir 'Salsa: $21 por pieza.'
								Escribir 'Frijoles: $40 por pieza.'
							4:
								Escribir 'Mostrando procedimientos.'
							De Otro Modo:
								Escribir 'Documento no valido.'
						FinSegún
					'3':
						Escribir 'DOCUMENTOS DISPONIBLES'
						Escribir '1. ventas.txt'
						Escribir '2. inventario.txt'
						Escribir '3. productos.txt'
						Escribir '4. procedimientos.txt'
						Escribir 'Seleccione el documento:'
						Leer seleccion
						Escribir 'Escriba la informacion que desea agregar:'
						Leer contenido
						Si contenido<>'' Entonces
							Escribir 'Fecha: ', dia, '/', mes, '/', anio
							Escribir 'Usuario: ', usuario
							Escribir 'Informacion agregada al final del documento.'
						SiNo
							Escribir 'El contenido no puede estar vacio.'
						FinSi
					'4':
						Escribir 'CREAR DOCUMENTO NUEVO'
						Escribir 'Ingrese el nombre del documento:'
						Leer documento
						Escribir 'Ingrese el contenido inicial:'
						Leer contenido
						Escribir 'Documento creado correctamente.'
						Escribir 'Fecha de creacion: ', dia, '/', mes, '/', anio
					'5':
						continuar <- Verdadero
						Mientras continuar=Verdadero Hacer
							Escribir '======================================'
							Escribir '        ADMINISTRAR INVENTARIO'
							Escribir '======================================'
							Escribir '1. Agregar existencias'
							Escribir '2. Restablecer inventario'
							Escribir '3. Consultar inventario'
							Escribir '4. Regresar al menu'
							Leer opcionProducto
							Según opcionProducto Hacer
								'1':
									Escribir '1. Arroz: ', inventarioArroz
									Escribir '2. Salsa: ', inventarioSalsa
									Escribir '3. Frijoles: ', inventarioFrijoles
									Escribir 'Seleccione el producto:'
									Leer seleccion
									Escribir 'Cantidad de piezas que desea agregar:'
									Leer cantidad
									Si cantidad>0 Entonces
										Según seleccion Hacer
											1:
												inventarioArroz <- inventarioArroz+cantidad
											2:
												inventarioSalsa <- inventarioSalsa+cantidad
											3:
												inventarioFrijoles <- inventarioFrijoles+cantidad
											De Otro Modo:
												Escribir 'Producto invalido.'
										FinSegún
										Escribir 'Inventario actualizado.'
									SiNo
										Escribir 'Cantidad invalida.'
									FinSi
								'2':
									Escribir 'Desea restablecer el inventario? si/no:'
									Leer respuesta
									Si respuesta='si' Entonces
										inventarioArroz <- 20
										inventarioSalsa <- 15
										inventarioFrijoles <- 25
										Escribir 'Inventario restablecido.'
									SiNo
										Escribir 'Operacion cancelada.'
									FinSi
								'3':
									Escribir 'INVENTARIO ACTUAL'
									Escribir 'Arroz: ', inventarioArroz, ' piezas'
									Escribir 'Salsa: ', inventarioSalsa, ' piezas'
									Escribir 'Frijoles: ', inventarioFrijoles, ' piezas'
								'4':
									continuar <- Falso
								De Otro Modo:
									Escribir 'Opcion invalida.'
							FinSegún
						FinMientras
					'6':
						Escribir 'Regresando a la pantalla inicial.'
						regresarInicio <- Verdadero
					'7':
						Escribir 'CERRANDO CAJA'
						salir <- Verdadero
					De Otro Modo:
						Escribir 'Opcion invalida. Intente nuevamente.'
				FinSegún
			FinSi
		FinMientras
	FinMientras
	Escribir '======================================'
	Escribir '              CIERRE DE CAJA'
	Escribir '======================================'
	Escribir 'Caja: ', caja
	Escribir 'Tickets registrados: ', cantidadTickets
	Escribir 'Dinero recaudado: $', dineroGanado
	Escribir 'INVENTARIO FINAL'
	Escribir 'Arroz: ', inventarioArroz
	Escribir 'Salsa: ', inventarioSalsa
	Escribir 'Frijoles: ', inventarioFrijoles
	Escribir 'RESUMEN DE PRODUCTOS'
	Escribir 'Tortillas vendidas: ', ventasTortilla
	Escribir 'Arroz vendido: ', ventasArroz
	Escribir 'Salsa vendida: ', ventasSalsa
	Escribir 'Frijoles vendidos: ', ventasFrijoles
	Escribir 'Gracias por utilizar el sistema.'
FinAlgoritmo
