def primeiras_ocorrencias(palavra):
    dic = {}
    dic[palavra[0]] = 0
    i = 0
    for letra in palavra:
        i += 1
        if letra not in dic.keys():
            dic[letra] = i-1
    return dic