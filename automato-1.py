alfabeto = []
estados = []
trans_func = {}
start = ""
end = []

alfabeto = str(input("Digite o alfabeto reconhecido pelo autômato, com os símbolos separados por espaços: ")).split()
estados = str(input("Digite os estados do autômato, separados por espaços: ")).split()
start = str(input("Agora qual desses estados é o estado inicial?: "))
while start not in estados:
	print("você digitou um estado inicial que não se enontra na lista de estados Q: {}.\nPor favor digite novamente".format(estados))
	start = str(input("Estado inicial: "))

end = str(input("E qual desses estados são finais? Digite separando-os por espaços: ")).split()
while True:
	estados_invalidos = []
	for estado in end:
		if estado not in estados:
			estados_invalidos.append(estado)
	if len(estados_invalidos) > 0:
		print("você digitou um ou mais estados q: '{}' finais que não se enontram na lista de estados Q: {}.\nPor favor digite-os novamente".format(estados_invalidos, estados))
		end = str(input("Estados finais: ")).split()
	elif len(estados_invalidos) == 0:
		break
