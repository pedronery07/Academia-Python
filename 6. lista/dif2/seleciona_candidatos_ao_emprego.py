def seleciona_candidatos(lcand, lcrit):
    if lcand == []:
        return []
    lsaida = []
    for i in range(len(lcand)):
        if len(lcand[i][2]) != 3:
            continue
        nome = lcand[i][0]
        rg = lcand[i][1]
        notas = lcand[i][2]
        if notas[0] >= lcrit[0] and notas[1] >= lcrit[1] and notas[2] >= lcrit[2]:
            lsaida.append([nome, rg])
    return lsaida
