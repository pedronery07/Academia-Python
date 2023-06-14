def eh_crescente(l):
    for i in range(len(l)-1):
        if l[i+1] > l[i]:
            continue
        else:
            return False
    return True