def produz_um_dois_insper(n0, nf, mult):
    l = []
    while n0 <= nf:
        if n0 % mult == 0:
            l.append('Insper')
        else:
            l.append(n0)
        n0 += 1
    return l