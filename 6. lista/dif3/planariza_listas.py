def junta_listas(l):
    junta = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            junta.append(l[i][j])
    return junta