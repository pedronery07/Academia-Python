def conta_palavras(string):
    dici = {}
    minusculas = string.lower()
    esp = "?!,."
    l = []
    for letra in minusculas:
        if letra in esp:
            continue
        else:
            l.append(letra)
    sem_esp = ''.join(l)
    palavras = sem_esp.split()
    for pal in palavras:
        if pal not in dici.keys():
            dici[pal] = 1
        else:
            dici[pal] += 1
    return dici