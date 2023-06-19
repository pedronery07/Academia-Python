def conserta_teclado(string):
    anterior = ''
    correcao = ''
    for letra in string:
        letra_padrao = letra.lower()
        if letra_padrao != anterior:
            correcao += letra_padrao
        anterior = letra_padrao
    return correcao