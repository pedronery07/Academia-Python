def interseccao_valores(d1, d2):
    l = []
    for v in d1.values():
        if v in d2.values():
            l.append(v)
    return l