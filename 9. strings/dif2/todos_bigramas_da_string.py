def acha_bigramas(string):
    l = []
    for i in range(len(string)-1):
        if string[i] + string[i+1] not in l:
            l.append(string[i] + string[i+1])
    return l