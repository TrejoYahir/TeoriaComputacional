#Creamos los menus
mensaje_entrada = "Hola, por favor ingresa el tipo de Alfabeto con el que trabajare:\n"
menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Numeros (0...9)\n')
print (mensaje_entrada + menu)
opcion = input()
print (opcion)
alfabeto = []
if opcion == '1':
	print ("Entre al if")
	seguir = 1
	while seguir==1:
		simbolo=input("Ingrese un simbolo\n")
		alfabeto.append(simbolo);
		if len(alfabeto)>2:
			seguir_agregando=1
			while seguir_agregando==1:	
				opcion2 = input("Desea ingresar más elementos s/n \n")
				if opcion2=='s':
					seguir_agregando=0
				elif opcion2=='n':
					seguir=0
					seguir_agregando=0
				else:
					pass
	print (alfabeto)