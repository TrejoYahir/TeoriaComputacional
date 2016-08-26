#Creamos los menus
def menu_entrada():
	mensaje_entrada = "Hola, por favor ingresa el tipo de Alfabeto con el que trabajaré:\n"
	menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Números (0...9)\n')
	#Imprimimos el menu
	print (mensaje_entrada)
	crear_alfabeto(menu)

#Función que crea el alfabeto dependiendo de la opción del usuario
def crear_alfabeto(menu):
	opcion_valida=True
	while opcion_valida:
		#Imprimimos el menu y obtenemos la opción
		opcion = input(menu)
		print (opcion+'\n')
		alfabeto = []
		#Dependiendo la opción es el menu a usar
		# 1- Alfabeto dinamico ingresado por el usuario
		if opcion == '1':
			opcion_valida=False
			seguir = True
			while seguir:
				simbolo=input("Ingrese un simbolo\n")
				alfabeto.append(simbolo)
				if len(alfabeto)>2:
					seguir_agregando=True
					while seguir_agregando:	
						opcion2 = input("Desea ingresar más elementos? s/n \n")
						if opcion2=='s':
							seguir_agregando=False
						elif opcion2=='n':
							seguir=False
							seguir_agregando=False
						else:
							pass
		#Alfabeto español
		elif opcion == '2':
			opcion_valida=False
			print ("El alfabeto es español")
			alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
		#Alfabeto númerico
		elif opcion == '3':
			opcion_valida=False
			print ("El alfabeto es númerico")
			alfabeto=['0','1','2','3','4','5','6','7','8','9']
		#Opción invalida se repite el ciclo
		else:
			print('Opción no valida, debe ser alguna de las siguientes\n')
	#Al final imprimimos el alfabeto
	print ("El alfabeto con el que trabajaré es:\n")
	print (alfabeto)
	print("\n")
	#Ahora pedimos que ingrese las palabras
	ingresar_palabras(alfabeto)

#Función para verificar dos palabras con respecto al alfabeto
def ingresar_palabras(alfabeto):
	palabra1=""
	palabra2=""
	while validar_palabra(alfabeto,palabra1):
		palabra1=input("Por favor ingrese una palabra:\n")			
		
#Función que valida si una palabra pertenece al alfabeto o no
def validar_palabra(alfabeto,palabra):
	if len(palabra)>0:
		variable_auxiliar=0
		for w in range(len(palabra)):
			for x in range(len(alfabeto)):
				if alfabeto[x] == palabra[w]:
					variable_auxiliar=variable_auxiliar+1
		if variable_auxiliar==len(palabra):
			print ("Palabra valida: "+palabra)
			return False
		else:
			print ("Palabra invalida")	
			return True
	else:
		return True


#Iniciamos el programa
menu_entrada()