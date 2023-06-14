def calcula_investimento(inv0,m,a):
    i = 1
    if a == "LCI":
        while i <= m:
            ac = inv0*(1.60/100)
            inv0 += ac
            i += 1
    elif a == "CDB":
        while i <= m:
            ac = inv0*(1.30/100)
            inv0 += ac
            if i%6 == 0:
                bonus = (1.20/100)*inv0
                inv0 += bonus
            i += 1
    elif a == "LCA":
        while i <= m:
            ac = inv0*(1.45/100)
            inv0 += ac
            if i%4 == 0:
                bonus = inv0*1/100
                inv0 += bonus
            i += 1
    return inv0 