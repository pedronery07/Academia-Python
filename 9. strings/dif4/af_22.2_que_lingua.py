def cleanup(txt):
    txt_limpo = ''
    especiais = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{']
    for letra in txt:
        if letra not in especiais:
            txt_limpo += letra.lower()
    return txt_limpo

def predizer_lingua(dic_linguas, txt):
    if dic_linguas == {}:
        return {'palpite': 'DESCONHECIDA'}
    proporcoes = {}
    if txt == '':
        for ling, p in dic_linguas.items():
            proporcoes[ling] = 0
        proporcoes['palpite'] = 'DESCONHECIDA'
        return proporcoes    
    for ling, p in dic_linguas.items():
        proporcoes[ling] = 0
    txt_limpo = cleanup(txt)
    l_palavras = txt_limpo.split()
    for pal in l_palavras:
        for ling, p in dic_linguas.items():
            if pal in p:
                proporcoes[ling] += 1
    retorno = {}
    i = 0
    maior = max(proporcoes.values())
    for k, v in proporcoes.items():
        if i == 0:
            maior = v/len(l_palavras)
            palp = k
            retorno[k] = v/len(l_palavras)
            i = 1
        else:
            if v/len(l_palavras) > maior:
                maior = v/len(l_palavras)
                palp = k
            retorno[k] = v/len(l_palavras)
    maximo = max(retorno.values())
    checa = 0
    for v in retorno.values():
        if v == maximo:
            checa += 1
    if checa != 0:
        retorno['palpite'] = 'DESCONHECIDA'    
    else:
        retorno['palpite'] = palp
    return retorno