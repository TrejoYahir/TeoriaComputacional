#Creamos los menus
mensaje_entrada = "Hola, por favor ingresa el tipo de Alfabeto con el que trabajaré:\n"
menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Números (0...9)\n')
opcion_valida=True
print (mensaje_entrada)
while opcion_valida:
	opcion = input(menu)
	print (opcion+'\n')
	alfabeto = []
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
	elif opcion == '2':
		opcion_valida=False
		print ("El alfabeto es español")
		alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
	elif opcion == '3':
		opcion_valida=False
		print ("El alfabeto es númerico")
		alfabeto=['0','1','2','3','4','5','6','7','8','9']
	else:
		print('Opción no valida, debe ser alguna de las siguientes\n')
print (alfabeto)