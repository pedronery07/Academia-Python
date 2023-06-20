def cleanup(txt):
    limpeza = []
    caracteres = "! ? , ; . ! ) } ] ( [ { :"
    l_caracteres = caracteres.split()
    for letra in txt:
        if letra not in l_caracteres:
            limpeza.append(letra)
    return ''.join(limpeza)

def extrair_placas(lista_textos):
    dici = {}
    indice_texto = 0
    info = {}
    if lista_textos == []:
        return dici
    for texto in lista_textos:
        limpo = cleanup(texto)
        palavras = limpo.split()
        for p in palavras:
            if len(p) == 7:
                # VERIFICA FORMATO MERCOSUL
                if p[:3].isalpha() and p[4].isalpha():
                    if p[3].isdigit() and p[5:].isdigit():
                        info['placa'] = p
                        info['indice_lista_texto'] = indice_texto
                        info['indice_palavra'] = palavras.index(p)
                        if 'mercosul' not in dici.keys():
                            dici['mercosul'] = [info]
                        else:
                            dici['mercosul'].append(info)
                # VERIFICA FORMATO ANTIGO
                elif p[:3].isalpha() and p[3:].isdigit():
                    info['placa'] = p
                    info['indice_lista_texto'] = indice_texto
                    info['indice_palavra'] = palavras.index(p)
                    if 'antigo' not in dici.keys():
                        dici['antigo'] = [info]
                    else:
                        dici['antigo'].append(info)
                info = {}
        indice_texto += 1
    return dici