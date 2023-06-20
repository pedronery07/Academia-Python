def mais_frequente(lpalavras):
    dici = {}
    for p in lpalavras:
        if p not in dici.keys():
            dici[p] = 1
        else:
            dici[p] += 1
    i = 0
    for palavra, n in dici.items():
        if i == 0:
            maior = n
            maisf = palavra
            i = 1
        else:
            if n > maior:
                maisf = palavra
                maior = n
    return maisf