T = 'O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse [1910–1995]. Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico.'

alfabeto = set(T)
#print(alfabeto)

q0 = dict()
q1 = dict()
q2 = dict()
q3 = dict()
q4 = dict()
q5 = dict()
q6 = dict()
q7 = dict()
q8 = dict()
q9 = dict()
q10 = dict()
q11 = dict()
q12 = dict()

#q0
for c in alfabeto:
    if c == ' ':
        q0[' '] = 1
    else: 
        q0[c] = 0
#q1
for c in alfabeto:
    if c == 'c':
        q1['c'] = 2
    else: 
        q1[c] = 0
#q2
for c in alfabeto:
    if c == 'o':
        q2['o'] = 3
    else: 
        q2[c] = 0
#q3
for c in alfabeto:
    if c == 'm':
        q3['m'] = 4
    else: 
        q3[c] = 0
#q4
for c in alfabeto:
    if c == 'p':
        q4['p'] = 5
    else: 
        q4[c] = 0
#q5
for c in alfabeto:
    if c == 'u':
        q5['u'] = 6
    else: 
        q5[c] = 0
#q6
for c in alfabeto:
    if c == 't':
        q6['t'] = 7
    else: 
        q6[c] = 0
#q7
for c in alfabeto:
    if c == 'a':
        q7['a'] = 8
    else: 
        q7[c] = 0
#q8
for c in alfabeto:
    if c == 'd':
        q8['d'] = 9
    else: 
        q8[c] = 0
#q9
for c in alfabeto:
    if c == 'o':
        q9['o'] = 10
    else: 
        q9[c] = 0
#q10
for c in alfabeto:
    if c == 'r':
        q10['r'] = 11
    else: 
        q10[c] = 0
#q11
for c in alfabeto:
    if c == ' ':
        q11[' '] = 12
    else:
        q11[c] = 0
#q12
for c in alfabeto:
    q12[c] = 0


dfa2 = {
    0:q0,
    1:q1,
    2:q2,
    3:q3,
    4:q4,
    5:q5,
    6:q6,
    7:q7,
    8:q8,
    9:q9,
    10:q10,
    11:q11,
    12:q12
}

#print(dfa2)

def accepts2(transitions, initial, state_final, s):
    state = initial

    for i in range(len(s)):
        if state == 0:
            position = None

        if s[i] == 'c': 
            position = i

        if position and state == 12:
            print(position)



        state = transitions[state][s[i]]
    return state in state_final


print(accepts2(dfa2, 0, {0}, T))
