def verifica_respiravel(contagens, total, nocivos):
    concentracoes = {}
    for gas, conc in contagens.items():
        if gas not in concentracoes.keys():
            concentracoes[gas] = (conc/total)*100
    for gas, conc in concentracoes.items():
        if gas == 'O':
            if conc < 20:
                if gas not in nocivos.keys():
                    nocivos[gas] = conc
        elif gas == 'N':
            if conc > 70:
                if gas not in nocivos.keys():
                    nocivos[gas] = conc
        else:
            if conc > 2:
                if gas not in nocivos.keys():
                    nocivos[gas] = conc
    if nocivos == {}:  
        return True
    else:
        return nocivos

def concentracao_nociva(atm):
    conta_o2 = 0
    conta_n = 0
    total = 0
    contagens = {}
    nocivos = {}
    for amostra in atm:
        for gases in amostra:
            for gas in gases:
                if gas == 'O':
                    conta_o2 += 1
                elif gas == 'N':
                    conta_n += 1
                if gas not in contagens.keys():
                    contagens[gas] = 1
                else:
                    contagens[gas] += 1
                total += 1
    if conta_o2 == 0:
        if 'O' not in nocivos.keys():
            nocivos['O'] = 0
    verificação = verifica_respiravel(contagens, total, nocivos)
    if verificação == True:
        return {}
    else:
        return verificação