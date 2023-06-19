def identifica_espaco(string):
    num = 0
    for letra in string:
        if letra == ' ':
            ind = string.index(letra)
            item = string[ind+1::]
            return [num, item]
        else:
            num += int(letra)

def contabiliza(colaboracoes):
    dici = {}
    for pessoa, itens in colaboracoes.items():
        for item in itens:
            l = identifica_espaco(item)
            if l[1] not in dici.keys():
                dici[l[1]] = l[0]
            else:
                dici[l[1]] += l[0]
    return dici
