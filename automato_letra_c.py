class Estado_q0:
    def __init__(self):
        self.nome = "q0"
    
    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q2()
        elif entrada == 'b':
            return Estado_q3()
        else:
            return EstadoDeRejeicao()

class Estado_q1():
    def __init__(self):
        self.nome = "q1"
    
    def transicao(self, entrada):
        if entrada == 'b':
            return Estado_q1()
        else:
            return EstadoDeRejeicao()
        
        
class Estado_q2:
    def __init__(self):
        self.nome = "q2"

    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q4()
        elif entrada == 'b':
            return Estado_q1()
        else: 
            return EstadoDeRejeicao()

class Estado_q3:
    def __init__(self):
        self.nome = "q3"
    
    def transicao(self, entrada):
        if len(entrada) > 0:
            return EstadoDeRejeicao()
        
class Estado_q4:
    def __init__(self):
        self.nome = "q4"
    
    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q4
        elif entrada == 'b':
            return Estado_q3()
        else:
            return EstadoDeRejeicao()

class EstadoDeRejeicao:
    def __init__(self):
        self.nome = "Rejeição"
    
    def transicao(self, entrada):
        return self


class Automato:
    def __init__(self):
        self.estado_atual = Estado_q0()
    
    def transicoes(self, cadeia):
        for entrada in cadeia:
            self.estado_atual = self.estado_atual.transicao(entrada)
    
    def executar(self, cadeia):
        self.transicoes(cadeia)
        if isinstance(self.estado_atual, Estado_q1):
            print("Cadeia aceita pelo automato")
        elif isinstance(self.estado_atual, Estado_q2):
            print("Cadeia aceita pelo automato")
        elif isinstance(self.estado_atual, Estado_q3):
            print("Cadeia aceita pelo automato")
        else:
            print("Cadeia rejeitada pelo automato")

automato = Automato()
automato.executar("")
automato.executar("a")
automato.executar("b")
automato.executar("aaab")
automato.executar("ab")
automato.executar("aabb")
automato.executar("aa")
automato.executar("aab")
automato.executar("aaaab")
automato.executar("abbb")
automato.executar("aba")
automato.executar("aabbb")
automato.executar("abb")
automato.executar("aaabb")
automato.executar("abbbb")
automato.executar("abaa")
automato.executar("aabbab")
automato.executar("abab")
automato.executar("aaaabb")
automato.executar("abbbbb")
