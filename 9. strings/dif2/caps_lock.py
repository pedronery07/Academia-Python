def capsLock(texto):
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    correcao = []
    for letra in texto:
        if letra in maiusculas:
            correcao.append(letra.lower())
        else:
            correcao.append(letra.upper())
    return "".join(correcao)