#Creamos los menus
# -*- coding: utf-8 -*-
mensaje_entrada = "Hola, por favor ingresa el tipo de Alfabeto con el que trabajare:\n"
menu = ('1.- Ingresar alfabeto manualmente\n'
	'2- Alfabeto Espaniol\n'
	'3.- Numeros (0...9)\n')
print mensaje_entrada + menu
opcion = input()
print opcion
alfabeto=[]
if opcion==1:
	seguir=1;
	while seguir:
		simbolo=raw_input("Ingrese una letra\n")
		alfabeto.append(simbolo);
		if len(alfabeto)>3:
			while opcion11:	
				print 
				opcion2 = raw_input("Desea ingresar más elementos s/n \n")
				if opcion2==s:
					pass
					opcion11=0
				elif opcion2==n:
					seguir=0
					opcion11=0
				else:
					pass
	print alfabeto			





		
	