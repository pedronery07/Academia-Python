def contabilizar(parametro, l):
    ml = 0
    for i in range(len(l)):
        vol = l[i][0]
        quant = l[i][1]
        ml += vol*quant
    return ml//parametro