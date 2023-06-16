def calcula_media(l):
    n = 0
    i = 0
    for turma in l:
        for nota in turma.values():
            n += nota
            i += 1
    return n/i