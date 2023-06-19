def palavras_com_tamanho_crescente(lista):
    tam = 0
    for string in lista:
        if len(string) <= tam:
            return False
        tam = len(string)
    return True