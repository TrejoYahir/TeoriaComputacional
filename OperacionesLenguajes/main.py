#Importamos las librerias a usar
import random
#Función principal
def main():
	mensaje_entrada = "Inciso a) de la práctica\nHola, por favor ingresa el tipo de Alfabeto con el que trabajare:\n"
	menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Numeros (0...9)\n')
	#Imprimimos el menu
	print (mensaje_entrada)
	#Inciso a)
	#Creamos el alfabeto
	alfabeto=crear_alfabeto(menu)
	#Al final imprimimos el alfabeto
	print ("El alfabeto con el que trabajare es:\n")
	print (alfabeto)
	print("\n")
	#Inciso b)
	#Ahora el programa automaticamente creará los lenguajes con los que se trabajará
	print("Lenguaje 1:\n")
	lenguaje1=crear_lenguaje(alfabeto)
	print("Lenguaje 2:\n")
	lenguaje2=crear_lenguaje(alfabeto)
	#Imprimimos los lenguajes
	print ("Los lenguajes con los que trabajare son:\n")
	print("Lenguaje 1:\nL1 = ",lenguaje1)
	print("\nLenguaje 2:\nL2 = ",lenguaje2)
	#Inciso c)
	#Imprimimos la union de los lenguajes
	print("\nLa union de ambos lenguajes es:\nLu=",union_lenguajes(lenguaje1,lenguaje2))
	#Inciso d)
	#Imprimimos la concatenacion de los lenguajes
	print("\nLa concatenacion de los lenguajes es:\nLc =",concatenacion_lenguajes(lenguaje1,lenguaje2))
	#Inciso e)
	#Imprimimos la diferencia entre ambos lenguajes
	print("\nLa diferencia de el lenguaje L1-L2 es:\nL1-L2 =", diferencia_lenguajes(lenguaje1,lenguaje2))
	print("\nLa diferencia de el lenguaje L2-L1 es:\nL2-L1 =", diferencia_lenguajes(lenguaje2,lenguaje1))
	#Inciso f)
	#Potencia de un lenguaje
	potencia_lenguaje_opcion(lenguaje1,lenguaje2)

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
	numero_elementos=pedir_n(1)
	print("Ahora, por favor ingrese la longitud de las palabras que compondran el alfabeto:\n")
	longitud=pedir_n(1)
	#Definimos a nuestro lenguaje
	lenguaje=set()
	aux=set()
	palabras=potencia_alfabeto(alfabeto,aux,longitud)
	#potencia_alfabeto(alfabeto,aux,longitud)
	lista_palabras=list(palabras)
	print("\n",lista_palabras,"\n")
	continuar=True
	while continuar:
		lista_lenguaje=list(lenguaje)
		if numero_elementos == len(lista_lenguaje):
			continuar=False
		else:
			aleatorio=random.randint(0,len(lista_palabras))
			if aleatorio >= len(lista_palabras):
				lenguaje.add(lista_palabras[aleatorio-1])
			else:
				print(aleatorio)
				lenguaje.add(lista_palabras[aleatorio])
	return lenguaje

#Funcion que le pide al usuario ingresar una n entera
def pedir_n(opcion):
	n=""
	if opcion == 1:
		while n_valida(n,1):
			n=input("Por favor ingrese un entero:\n")
	else:
		while n_valida(n,0):
			n=input("Por favor ingrese un entero:\n")
	#La función input siempre devuelve un string, así que lo convertimos a int
	return int(n)

#Función que verifica si n es un numero entero valido o no
def n_valida(n,opcion):
	try:
		int(n)
		if (int(n) in range(-6,6)) == False:
			print ("\nn fuera de rango\n")
			return True
		return False
	except ValueError:
		return True

#Funcion que calcula la potencia n de un alfabeto
def potencia_alfabeto(alfabeto,aux,n):
	#Distintos casos de n
	n=abs(n)
	potencia=set()
	lista_alfabeto=list(alfabeto)
	if n==0:
		potencia.add("Cadena vacia")
		print (potencia)
		return potencia
	#n mayor o igual 1
	else:
		auxiliar=list(aux)
		if len(auxiliar) == 0:
			auxiliar=list(alfabeto)
			aux=alfabeto
		if len(auxiliar) == (len(lista_alfabeto)**n):
			print("Numero de elementos:\n")
			print(len(auxiliar))
			print("\nElementos:\n")
			print(aux)
			return aux
		else:
			for i in range(len(auxiliar)):
				for j in range(len(lista_alfabeto)):
					potencia.add(auxiliar[i]+lista_alfabeto[j])
			return potencia_alfabeto(alfabeto,potencia,n)

#Funcion que une dos lenguajes
def union_lenguajes(lenguaje1,lenguaje2):
	return lenguaje1|lenguaje2

#Funcion que concatena dos lenguajes
def concatenacion_lenguajes(lenguaje1,lenguaje2):
	concatenacion=set()
	for i in lenguaje1:
		for j in lenguaje2:
			concatenacion.add(i+j)
	return concatenacion

#Funcion que hace la diferencia (resta) entre dos lenguajes
def diferencia_lenguajes(lenguaje1,lenguaje2):
	return lenguaje1-lenguaje2

#Funcion que le permite al usuario escoger el lenguaje y la potencia(la n) para realizar la potencia del mismo
def potencia_lenguaje_opcion(lenguaje1,lenguaje2):
	#Le pedimos al usuario que seleccione un lenguaje
	opcion_valida=True
	while opcion_valida:
		print("\nPor favor, ahora seleccione un alfabeto al cual le aplicare la potencia\n")
		opcion=input("1 -> Lenguaje1\n2 -> Lenguaje2\n")
		if opcion == "1":
			opcion_valida=False
			print("\nPor favor ingrese el numero al cual se aplicara la potencia para el alfabeto [-5,5]\n")
			n=pedir_n(0)
			potencia_lenguaje(lenguaje1,n)
		elif opcion == "2":
			opcion_valida=False
			print("\nPor favor ingrese el numero al cual se aplicara la potencia para el alfabeto [-5,5]\n")
			n=pedir_n(0)
			potencia_lenguaje(lenguaje2,n)
		else:
			print("Opcion no valida, debe ser 1 o 2")

#Potencia de un lenguaje
def potencia_lenguaje(lenguaje,n):
	potencia=set()
	#n=0
	if n == 0:
		potencia.add("Cadena Vacia")
		print("\nLp = ",potencia,"\n")
	#n>0
	elif n>0:
		lista_potencia=list(potencia)
		if len(lista_potencia) == 0:
			potencia=lenguaje
		for i in range(n-1):
			potencia= concatenacion_lenguajes(potencia,lenguaje)
		print("\nLp = ",potencia)
	#n<0
	else:
		auxiliar=set()
		for i in lenguaje:
			auxiliar.add(i[::-1])
		n=abs(n)
		lista_potencia=list(potencia)
		if len(lista_potencia) == 0:
			potencia=auxiliar
		for i in range(n-1):
			potencia= concatenacion_lenguajes(potencia,auxiliar)
		print("\nLp = ",potencia)

#Funcion que crea un curp



#Ejecutamos el programa
main()