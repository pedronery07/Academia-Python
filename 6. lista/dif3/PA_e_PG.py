def verifica_progressao(l):
    PA = 0
    PG = 0
    l_teste1 = [l[len(l)-1]]
    l_teste2 = [l[len(l)-1]]
    if len(l) < 2:
        return "AG"
    else:
        r = l[1] - l[0]
        if l[0] != 0:
            q = l[1]/l[0]
        else:
            q = 0
    j = len(l) - 1
    while j > 0:
        if r != 0:
            l_teste1.append(l[j] - r) 
        if q != 0 and q != 1:
            l_teste2.append(l[j]/q)    
        j -= 1
    l_teste1.reverse()
    l_teste2.reverse()
    if l_teste1 == l:
        return 'PA'
    elif l_teste2 == l:
        return 'PG'
    elif r == 0 and q == 1:
        return 'AG'
    else:
        return 'NA'