def adiciona_na_mesa(peca,mesa):
    n1 = peca[0]
    n2 = peca[1]
    invertida = [n2, n1]
    if mesa == []:
        mesa.append(peca)
    elif len(mesa) == 1:
        if mesa[0][0] == n1:
            mesa.insert(0, invertida)
        elif mesa[0][0] == n2:
            mesa.insert(0, peca)
        elif mesa[0][1] == n1:
            mesa.append(peca)
        else:
            mesa.append(invertida)
    elif mesa[len(mesa)-1][1] == n2:
        mesa.append(invertida)
    elif mesa[len(mesa)-1][1] == n1:
        mesa.append(peca)
    elif mesa[0][0] == n2:
        mesa.insert(0, peca)
    else:
        mesa.insert(0, invertida)
    return mesa