from automata import Automata
def main():
	auto=Automata()
	archivo=open("prueba2.java","r")
	for line in archivo.readlines():
		if ("0" in line or "1" in line or "2" in line or "3" in line or "4" in line or "5" in line or "6" in line or "7" in line or "8" in line or "9" in line):
			#Creamos el automata cada vez que lo necesitemos
			auto=Automata()
			for c in line:
				print (c)
				auto.calcular_estado(c)
				print (auto.estado)
main()