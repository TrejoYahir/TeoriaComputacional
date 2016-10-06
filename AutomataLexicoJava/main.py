def main():
	archivo=open("prueba.java","r")
	for line in archivo.readlines():
		if "=" in line:
			automata_lexico(line)

main()