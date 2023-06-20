def pontos_no_skate(manobras, performances):
    especiais = ['!', '?', ',', ';', '.', ':', ')', '}', ']', '(', '[', '{']
    performances_limpo = {}
    manobras_padrao = {}
    # Deixa chaves do dicionario em minúsculas e pontos em formato de inteiro
    for man, points in manobras.items():
        minusculo = man.lower()
        espaco = points.index(' ')
        int_points = int(points[0:espaco])
        manobras_padrao[minusculo] = int_points 
    # Ajusta as frases
    for skatista, info in performances.items():
        if skatista not in performances_limpo.keys():
            performances_limpo[skatista] = []
        for f in info['frases']:
            frase_limpa = ''
            palavra_limpa = ''
            palavras = f.split()
            for pal in palavras:
                for letra in pal:
                    if letra not in especiais:
                        palavra_limpa += letra.lower()
                frase_limpa += palavra_limpa + ' '
                palavra_limpa = ''
            performances_limpo[skatista].append(frase_limpa)
            frase_limpa = ''
    # Análise das frases e pontuações
    pontuações = {}
    for skatista, frases in performances_limpo.items():
        padrao = {
            "qtde manobras": 0,
            "total pontos": 0}
        pontos = 0
        qtde_manobras = 0
        for frase in frases:
            palavras = frase.split()
            for p in palavras:
                if p in manobras_padrao.keys():
                    pontos += manobras_padrao[p]
                    qtde_manobras += 1
        padrao['qtde manobras'] = qtde_manobras
        padrao['total pontos'] = pontos
        if skatista not in pontuações.keys():
            pontuações[skatista] = padrao
    return pontuações