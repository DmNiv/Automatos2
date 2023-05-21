class Automato:
	def __init__(self, q, Σ, estado_inicial, estado_final):
		self.estados = q
		self.alfabeto = Σ
		self.trans_func = {}
		self.start = estado_inicial
		self.end = estado_final

	def processo(self, cadeia):
		estado_atual = self.start
		for simbolo in cadeia:
			if (estado_atual, simbolo) in self.trans_func:
				estado_atual = self.trans_func[(estado_atual, simbolo)]
			else:
				print("O autômato não reconhece a cadeia '{}' pois há uma transição inválida.\n".format(cadeia))
				return False
		if estado_atual in self.end:
			print("O autômato lê a cadeia '{}'.\n".format(cadeia))
			return estado_atual in self.end
		else:
			print("O autômato não lê a cadeia '{}' pois não termina em um estado final.\n".format(cadeia))
			return estado_atual in self.end

	def adicionar_trans_func(self, estado, simbolo, estado_destino):
		self.trans_func[(estado, simbolo)] = estado_destino


estados = list(set(str(input("Digite os estados do autômato, separados por espaços: ")).split()))

alfabeto = list(set(str(input("Digite o alfabeto reconhecido pelo autômato, com os símbolos separados por espaços: ")).split()))

start = str(input("Agora qual desses estados é o estado inicial?: "))

while start not in estados:
	print("você digitou um estado inicial que não se enontra na lista de estados Q: {}.\nPor favor digite novamente".format(estados))
	start = str(input("Estado inicial: "))

end = list(set(str(input("E qual desses estados são finais? Digite separando-os por espaços: ")).split()))

while True:
	estados_invalidos = []
	for estado in end:
		if estado not in estados:
			estados_invalidos.append(estado)
	if len(estados_invalidos) > 0:
		print("você digitou um ou mais estados q: '{}' finais que não se enontram na lista de estados Q: {}.\nPor favor digite-os novamente".format(estados_invalidos, estados))
		end = list(set(str(input("Estados finais: ")).split()))
	elif len(estados_invalidos) == 0:
		break

automato1 = Automato(estados, alfabeto, start, end)

print("Por fim, vamos inserir as transições do autômato, no formato 'estado simbolo estado_destino'.")

while True:
	opcao = input("Digite a transição ou digite 'sair' para encerrar: ")
	if opcao == "sair":
		break
	estado, simbolo, estado_destino = opcao.split()
	if estado not in estados or simbolo not in alfabeto or estado_destino not in estados:
		print("Você digitou um estado de leitura, símbolo ou estado destino que não se encontra na lista. Por favor digite a função de transição novamente.")
		continue
	automato1.adicionar_trans_func(estado, simbolo, estado_destino)

while True:
	entrada = str(input("Digite a sentença que o autômato deve reconhecer ou digite 'sair' para encerrar: "))
	if entrada == "sair":
		break
	resultado = automato1.processo(entrada)
