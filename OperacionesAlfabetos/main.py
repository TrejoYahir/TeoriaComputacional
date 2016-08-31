#Creamos los menus
def main():
	mensaje_entrada = "Inciso a) de la práctica\nHola, por favor ingresa el tipo de Alfabeto con el que trabajaré:\n"
	menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Números (0...9)\n')
	#Imprimimos el menu
	print (mensaje_entrada)
	#Creamos el alfabeto
	alfabeto=crear_alfabeto(menu)
	#Al final imprimimos el alfabeto
	print ("El alfabeto con el que trabajaré es:\n")
	print (alfabeto)
	print("\n")
	#Ahora solicitamos las palabras
	palabra1=ingresar_palabra(alfabeto)
	palabra2=ingresar_palabra(alfabeto)
	print("Las palabras con las que trabajaré son: w1 = "+palabra1+" y w2 = "+palabra2)
	#Ahora concatenamos las palabras
	concatenacion=concatenar_palabras(palabra1,palabra2)
	#Pedimos al usuario que ingrese n
	n=pedir_n()
	#Ejecutamos la potencia de la concatenacion
	potencia_palabra=potencia(concatenacion,n)
	print("El resultado de la potencia de la concatenacion es:\n"+potencia_palabra+"\n")
	print("La longitud de esta potencia es:\n "+longitud_palabra(alfabeto,potencia_palabra)+"\n")

#Función que crea el alfabeto dependiendo de la opción del usuario
def crear_alfabeto(menu):
	opcion_valida=True
	while opcion_valida:
		#Imprimimos el menu y obtenemos la opción
		opcion = input(menu)
		#Esto es un Set en python
		alfabeto = set()
		#Dependiendo la opción es el menu a usar
		# 1- Alfabeto dinamico ingresado por el usuario
		if opcion == '1':
			opcion_valida=False
			seguir = True
			while seguir:
				simbolo=input("Ingrese un simbolo\n")
				if simbolo != "":
					alfabeto.add(simbolo)
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
							return alfabeto
						else:
							pass
		#Alfabeto español
		elif opcion == '2':
			opcion_valida=False
			print ("El alfabeto es español")
			alfabeto={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}
			return alfabeto
		#Alfabeto númerico
		elif opcion == '3':
			opcion_valida=False
			print ("El alfabeto es númerico")
			alfabeto={'0','1','2','3','4','5','6','7','8','9'}
			return alfabeto
		#Opción invalida se repite el ciclo
		else:
			print('Opción no valida, debe ser alguna de las siguientes\n')

#Función para verificar dos palabras con respecto al alfabeto
def ingresar_palabra(alfabeto):
	palabra=""
	while validar_palabra(alfabeto, palabra):
		palabra=input("Por favor ingrese una palabra (w) :\n")
	return palabra

#Función que valida si una palabra pertenece al alfabeto o no
def validar_palabra(alfabeto,palabra):
	if len(palabra)>0:
		variable_auxiliar=0
		print("Son más caracteres\n")
		for i in alfabeto:
			for j in range(len(palabra)):
				if i==palabra[j:len(i)+j]:
					variable_auxiliar=variable_auxiliar+len(i)
		if variable_auxiliar==len(palabra):
			print ("Palabra valida\n")
			return False
		else:
			print ("Palabra invalida\n")
			return True
	else:
		return True

#Funcion que le pide al usuario ingresar una n entera
def pedir_n():
	n=""
	while n_valida(n):
		n=input("Ingrese un entero al que se elevara la concatenación:\n")
	#La función input siempre devuelve un string, así que lo convertimos a int
	n=int(n)
	return n

#Funcion que concatena dos palabras
def concatenar_palabras(palabra1,palabra2):
	return palabra1+palabra2

#Función que verifica si n es un numero entero valido o no
def n_valida(n):
	try:
		int(n)
		return False
	except ValueError:
		return True

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

#Funcion que imprime la longitud de una palabra
def longitud_palabra(alfabeto,palabra):
	#Aqui voy 

#Iniciamos el programa
main()