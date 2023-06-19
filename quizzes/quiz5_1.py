def analise_morfologica(string):
    if string == '':
        return {
    'adverbio': '0.00%',
    'preposicao': '0.00%',
    'conjuncao': '0.00%',
    'outras': '0.00%'
    }
    adverbios = 'sim não jamais nunca abaixo acima adentro adiante afora aí além aqui atrás dentro embaixo externamente lá longe perto afinal agora amanhã antes ontem breve cedo constantemente depois enfim hoje imediatamente jamais nunca sempre outrora primeiramente tarde provisoriamente sucessivamente já possivelmente provavelmente talvez bastante demais mais menos bem muito quanto quão quase tanto pouco demasiado imenso'
    adv_lista = adverbios.split()
    prep = 'à ante após até com contra de desde em entre para per perante por sem sob sobre trás'
    prep_lista = prep.split()
    conj = 'e mas ou pois que como quanto'
    conj_lista = conj.split()
    minusculas = string.lower()
    esp = '!?;.,:'
    l = []
    for letra in minusculas:
        if letra not in esp:
            l.append(letra)
    cleanup = ''.join(l)
    l_palavras = cleanup.split()
    total = 0
    conta_adv = 0
    conta_prep = 0
    conta_conj = 0
    conta_out = 0
    for p in l_palavras:
        if p in adv_lista:
            conta_adv += 1
        elif p in prep_lista:
            conta_prep += 1
        elif p in conj_lista:
            conta_conj += 1
        else:
            conta_out += 1
        total += 1
    dici = {
    'adverbio': '%',
    'preposicao': '%',
    'conjuncao': '%',
    'outras': '%'
    }
    dici['adverbio'] = f'{(conta_adv/total)*100:.2f}%'
    dici['preposicao'] = f'{(conta_prep/total)*100:.2f}%'
    dici['conjuncao'] = f'{(conta_conj/total)*100:.2f}%'
    dici['outras'] = f'{(conta_out/total)*100:.2f}%'
    return dici