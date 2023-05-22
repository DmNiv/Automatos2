#criar um dicionário em que as chaves sejam os estados e os valores sejam outros dicionários contendo o caracter lido e o estado alvo.

#exemplo de dicionário.
#imagem do automáto: https://i.stack.imgur.com/s7uO2.png
dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}

#função de validação. Ela recebe as transições, o estado inicial, um conjunto/lista contendo os estados finais e cadeia a ser lida.
#retorna true or false
def accepts(transitions, initial, state_final, s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in state_final

#exemplos
print(accepts(dfa,0,{0},'1011101'))
print(accepts(dfa,0,{0},'10111011'))
