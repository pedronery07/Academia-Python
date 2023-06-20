def cleanup(txt):
    especiais = [',', '?', '!', ';', '.', ':']
    txt_limpo = ''
    for caracter in txt:
        if caracter not in especiais:
            txt_limpo += caracter.lower()
    return txt_limpo

def verifica_ganhador(txt, jogadores):
    txt_clean = cleanup(txt)
    palavras = txt_clean.split()
    results = {}
    for jogador, palpites in jogadores.items():
        pontos = 0
        for palavra in palpites:
            pontos += palavras.count(palavra)
        if jogador not in results.keys():
            results[jogador] = pontos
    return results