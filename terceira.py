def Aceita(transitions, trans_saida, start, end, cadeia):
    state = start
    string_saida = ''
    print('(Estado atual, Simbolo)')
    for simbolo in cadeia:
        try:
            print(f"({state}, {simbolo}) -> ", end='')
            string_saida += trans_saida[state][simbolo]
            state = transitions[state][simbolo]
        except KeyError:
            print(f'Moeda recusada: {simbolo}')
            return False
    print(f'({state}, λ)')
    print('Cadeia de saída: ', string_saida)
    return state in end


start = 0
end = [25, 50, 75, 100]
trans_func = {
    0: {
        25: 25,
        50: 50,
        100: 100,
    },
    25: {
        25: 50,
        50: 75,
        100: 25,
    },
    50: {
        25: 75,
        50: 100,
        100: 50,
    },
    75: {
        25: 100,
        50: 25,
        100: 75,
    },
    100: {
        25: 25,
        50: 50,
        100: 100,
    }

}
trans_saida = {
    0: {
        25: '0',
        50: '0',
        100: '1',
    },
    25: {
        25: '0',
        50: '0',
        100: '1',
    },
    50: {
        25: '0',
        50: '1',
        100: '1',
    },
    75: {
        25: '1',
        50: '1',
        100: '1',
    },
    100: {
        25: '0',
        50: '0',
        100: '1',
    }
}
user_choice = 0
print('Moedas aceitas: 25, 50, 100')
moedas_inseridas = []
while True:
    user_choice = int(input('Insira uma moeda (0 para sair):'))
    if user_choice == 0:
        break
    moedas_inseridas.append(user_choice)

Aceita(trans_func, trans_saida, start, end, moedas_inseridas)
