def conta_letras(palavra):
    dic = {}
    for p in palavra:
        if p not in dic.keys():
            dic[p] = 1
        else:
            dic[p] += 1
    return dic