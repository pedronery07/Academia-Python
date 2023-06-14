def soma_pecas(l):
    s = 0
    for i in range(len(l)):
        s += sum(l[i])
    return s