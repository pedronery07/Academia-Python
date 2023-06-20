def calcula_escola(l):
    s = 0
    for i in range(len(l)):
        s += sum(l[i]) - min(l[i]) 
    return s