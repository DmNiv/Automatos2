class Estado_q0:
    def __init__(self):
        self.nome = "q0"
    
    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q1()
        elif entrada == 'b':
            return Estado_q2()
        else:
            return EstadoDeRejeicao()

class Estado_q1():
    def __init__(self):
        self.nome = "q1"
    
    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q3()
        elif entrada == 'b':
            return Estado_q4()
        else:
            return EstadoDeRejeicao()
        
        
class Estado_q2:
    def __init__(self):
        self.nome = "q2Estado_q2"

    def transicao(self, entrada):
        if entrada == "a" or "b":
            return EstadoDeRejeicao()

class Estado_q3:
    def __init__(self):
        self.nome = "q3"
    
    def transicao(self, entrada):
        if entrada == 'a':
            return Estado_q3()
        elif entrada == 'b':
            return Estado_q2()
        else:
            return EstadoDeRejeicao()
        
class Estado_q4:
    def __init__(self):
        self.nome = "q4Estado_q4"
    
    def transicao(self, entrada):
        if entrada == 'b':
            return Estado_q4()
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
        elif isinstance(self.estado_atual, Estado_q4):
            print("Cadeia aceita pelo automato")
        else:
            print("Cadeia rejeitada pelo automato")

automato = Automato()
automato.executar("")
