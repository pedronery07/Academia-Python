def palavras_sao_iguais(string):
    if "-" not in string:
        return False
    p1 = []
    p2 = []
    i = 0
    for letra in string:
        if letra == "-":
            pal1 = "".join(p1)
            i = 1
        elif i == 1:
            p2.append(letra)
        else:
            p1.append(letra)
    pal2 = "".join(p2)
    if pal1 == pal2:
        return True
    else:
        return False