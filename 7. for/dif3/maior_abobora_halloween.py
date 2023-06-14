def maior_abobora(especie,lista):
    peso = []
    ref = 0
    fazendeiro = 0
    c = 0
    n = 0
    num = 0
    if lista == [[]]:
        return -1 
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j][1] == especie:
                num += 1
                peso.append(lista[i][j][0])
            while c < len(peso):
                if peso[c] > n:
                    n = peso[c]
                c += 1
            if n > ref:
                ref = n
                fazendeiro = i
            c = 0
            n = 0
            peso = []
    if num == 0:
        return -1
    else:
        return fazendeiro