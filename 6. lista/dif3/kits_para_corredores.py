def organiza_filas(l):
    fila = [[],[],[],[]]
    for i in range(len(l)):
        idade = l[i][1]
        nome = l[i][0]
        if idade <= 20:
            fila[0].append(nome)
        elif idade > 20 and idade <= 40:
            fila[1].append(nome)
        elif idade > 40 and idade <= 60:
            fila[2].append(nome)
        else:
            fila[3].append(nome)
    return fila