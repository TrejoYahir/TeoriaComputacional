#Creamos los menus
def menu_entrada():
	mensaje_entrada = "Inciso a) de la práctica\nHola, por favor ingresa el tipo de Alfabeto con el que trabajaré:\n"
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
		#Esto es un Set en python
		alfabeto = []
		#Dependiendo la opción es el menu a usar
		# 1- Alfabeto dinamico ingresado por el usuario
		if opcion == '1':
			opcion_valida=False
			seguir = True
			while seguir:
				simbolo=input("Ingrese un simbolo\n")
				if simbolo != "":
					alfabeto.append(simbolo)
				else:
					print("Caracter no valido\n")
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
			alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','palabra','x','y','z']
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
	palabra1,palabra2="",""
	while validar_palabra(alfabeto, palabra1):
		palabra1=input("Inciso b) de la práctica\nPor favor ingrese una palabra (w1) :\n")
	while validar_palabra(alfabeto, palabra2):
		palabra2=input("Por favor ingrese otra palabra (w2) :\n")			
	print ("Estan son las palabras que ingresaste:\n"+palabra1+" "+palabra2)
	#Ejecutamos el inciso c de la práctica
	concatenacion_a_la_n(palabra1,palabra2)

#Función que valida si una palabra pertenece al alfabeto o no
def validar_palabra(alfabeto,palabra):
	if len(palabra)>0:
		variable_auxiliar=0
		#Esto funciona bien si el alfabeto son de un solo caracter
		for i in range(len(palabra)):
			for j in range(len(alfabeto)):
				if alfabeto[j] == palabra[i]:
					variable_auxiliar=variable_auxiliar+1
		if variable_auxiliar==len(palabra):
			print ("Palabra valida\n")
			return False
		#else:
		#	for i in range(len(alfabeto))
		#		auxiliar=0
				
		else:
			print ("Palabra invalida\n")	
			return True
	else:
		return True

def concatenacion_a_la_n(palabra1,palabra2):
	#Le pedimos al usuario que ingrese el valor de n 
	print("Inciso c de la práctica\n")
	#Pedimos al usuario que ingrese el valor hasta que sea un valor valido
	n=pedir_n()
	#Concatenamos las palabras
	concatenacion=concatenar_palabras(palabra1,palabra2)
	#Aplicamos la potencia a nuestra concatenacion
	potencia_palabra=potencia(concatenacion,n)
	print("El resultado de la potencia es:\n"+potencia_palabra+"\n")
	#Ahora calculamos la longitud de la potencia
	print ("Inciso d)\n")
	#longitud_palabra(potencia_palabra)

#Funcion que le pide al usuario ingresar una n entera
def pedir_n():
	n=""
	while n_valida(n):
		n=input("Ingrese un entero al que se elevara la concatenación:\n")
	#La función input siempre devuelve un string, así que lo convertimos a int
	n=int(n)
	return n

#Función que verifica si n es un numero entero valido o no
def n_valida(n):
	try:
		int(n)
		return False
	except ValueError:
		return True

#Funcion que concatena dos palabras
def concatenar_palabras(palabra1,palabra2):
	return palabra1+palabra2

#Funcion que imprime la longitud de una palabra
#def longitud_palabra(palabra):
	

#Funcion que le aplica la n potencia a alguna palabra
def potencia(palabra,n):
	potencia=""
	#Tenemos que evaluar para los 3 distintos caso de n
	if n==0:
		return "Cadena vacia"
	elif n>0:
		for i in range(n):
			potencia=potencia+palabra
	#Por default, debe ser n negativa
	else:
		#Hay que voltear la cadena
		palabra=palabra[::-1]
		for i in range(abs(n)):
			potencia=potencia+palabra 
	return potencia

#Iniciamos el programa
menu_entrada()