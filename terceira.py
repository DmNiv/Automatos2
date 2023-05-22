def Aceita(transitions, trans_saida, start, end, cadeia):
    state = start
    string_saida = ''
    for simbolo in cadeia:
        try:
            string_saida += trans_saida[state][simbolo]
            state = transitions[state][simbolo]
        except KeyError:
            print(f'Valor não faz parte do alfabeto: {simbolo}')
            return False
    print(string_saida)
    return state in end


start = 0
end = [0, 25, 75, 100]
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
print(Aceita(trans_func, trans_saida, start,
      end, [50, 25, 50, 100, 25, 50, 100]))
