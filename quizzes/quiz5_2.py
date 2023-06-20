def quanto_tempo(tempo):
    caracteres = ['m', 's', 'h']
    conta_tempo = {'h': 0, 's':0, 'm':0}
    total = ''
    # Percorre lista de tempos
    for time in tempo:
        t = ''
        # Percorre digitos de cada tempo na lista
        for digito in time:
            # Verifica se é um número ou indicador de tempo
            if digito in caracteres:
                t = int(t)
                # Insere no dicionário de tempos
                if digito == 'm':
                    conta_tempo[digito] += t
                elif digito == 's':
                    conta_tempo[digito] += t
                elif digito == 'h':
                    conta_tempo[digito] += t
                t = ''
            else:
                t += digito
    for j, k in conta_tempo.items():
        while k > 59 and j == 's':
            conta_tempo[j] -= 60
            k -= 60
            conta_tempo['m'] += 1
        while k > 59 and j == 'm':
            conta_tempo[j] -= 60
            k -= 60
            conta_tempo['h'] += 1
    # Remove zeros, se existirem, e cria retorno
    minutos = conta_tempo['m']
    h = conta_tempo['h']
    seg = conta_tempo['s']
    l = [h, minutos, seg]
    if l[0] != 0:
        total += str(l[0]) + 'h'
    if l[1] != 0:
        total += str(l[1]) + 'm'
    if l[2] != 0:
        total += str(l[2]) + 's'
    return total