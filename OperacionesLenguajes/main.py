#Importamos las librerias a usar
import random
#Función principal
potencia=set()
def main():
	mensaje_entrada = "Inciso a) de la práctica\nHola, por favor ingresa el tipo de Alfabeto con el que trabajare:\n"
	menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Numeros (0...9)\n')
	#Imprimimos el menu
	print (mensaje_entrada)
	#Creamos el alfabeto
	alfabeto=crear_alfabeto(menu)
	#Al final imprimimos el alfabeto
	print ("El alfabeto con el que trabajare es:\n")
	print (alfabeto)
	print("\n")
	#Ahora el programa automaticamente creará los lenguajes con los que se trabajará
	print("Lenguaje 1:\n")
	lenguaje1=crear_lenguaje(alfabeto)
	print("Lenguaje 2:\n")
	lenguaje2=crear_lenguaje(alfabeto)
	#Imprimimos los lenguajes
	print ("Los lenguajes con los que trabajare son:\n")
	print("Lenguaje 1:\n ",lenguaje1)
	print("\nLenguaje 2:\n ",lenguaje2)

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
				if simbolo != "" and (" " in simbolo)==False:
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
			print ("El alfabeto es espaniol")
			alfabeto={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'}
			return alfabeto
		#Alfabeto númerico
		elif opcion == '3':
			opcion_valida=False
			print ("El alfabeto es numerico")
			alfabeto={'0','1','2','3','4','5','6','7','8','9'}
			return alfabeto
		#Opción invalida se repite el ciclo
		else:
			print('Opcion no valida, debe ser alguna de las siguientes\n')

#Funcion que crea un lenguaje a partir de un alfabeto
def crear_lenguaje(alfabeto):
	#Solicitamos el numero de elementos y la longitud de los mismos para el alfabeto
	print("Por favor ingrese la cantidad de palabras que contendra el alfabeto:\n")
	numero_elementos=pedir_n()
	print("Ahora, por favor ingrese la longitud de las palabras que compondran el alfabeto:\n")
	longitud=pedir_n()
	#Definimos a nuestro lenguaje
	lenguaje=set()
	aux=set()
	potencia_alfabeto(alfabeto,aux,longitud)
	lista_palabras=list(potencia)
	print("\n",lista_palabras,"\n")
	continuar=True
	while continuar:
		lista_lenguaje=list(lenguaje)
		if numero_elementos == len(lista_lenguaje):
			continuar=False
		else:
			lenguaje.add(lista_palabras[random.randint(0,len(lista_palabras))])
	return lenguaje


#Funcion que le pide al usuario ingresar una n entera
def pedir_n():
	n=""
	while n_valida(n):
		n=input("Por favor ingrese un entero:\n")
	#La función input siempre devuelve un string, así que lo convertimos a int
	return int(n)

#Función que verifica si n es un numero entero valido o no
def n_valida(n):
	try:
		int(n)
		return False
	except ValueError:
		return True

#Funcion que calcula la potencia n de un alfabeto
def potencia_alfabeto(alfabeto,aux,n):
	#Distintos casos de n
	n=abs(n)
	#potencia=set()
	lista_alfabeto=list(alfabeto)
	if n==0:
		potencia.add("Cadena vacia")
		print (potencia)
	#n mayor o igual 1
	else:
		auxiliar=list(aux)
		if len(auxiliar) == 0:
			auxiliar=list(alfabeto)
			aux=alfabeto
		if len(auxiliar) == (len(lista_alfabeto)**n):
			pass
			#print("Numero de elementos:\n")
			#print(len(auxiliar))
			#print("\nElementos:\n")
			#print(aux)
		else:
			for i in range(len(auxiliar)):
				for j in range(len(lista_alfabeto)):
					potencia.add(auxiliar[i]+lista_alfabeto[j])
			potencia_alfabeto(alfabeto,potencia,n)

#Ejecutamos el programa
main()