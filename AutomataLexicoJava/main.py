from automata import Automata
def main():
	auto=Automata()
	archivo=open("prueba.java","r")
	for line in archivo.readlines():
		if ("0" in line or "1" in line or "2" in line or "3" in line or "4" in line or "5" in line or "6" in line or "7" in line or "8" in line or "9" in line):
			for c in line:
				auto.calcular_estado(c)
			print(auto.estado)
main()