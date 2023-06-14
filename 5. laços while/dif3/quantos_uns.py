def quantos_uns(n):
    cont = 0
    a = str(n)
    for i in range(len(a)):
        if a[i] == '1':
            cont += 1
    return cont