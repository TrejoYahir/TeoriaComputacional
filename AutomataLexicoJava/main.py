def main():
	archivo=open("prueba.java","r")
	for line in archivo.readlines():
		if "=" in line:
			print (line)
main()