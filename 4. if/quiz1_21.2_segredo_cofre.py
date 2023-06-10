def calcula_segredo(num):
    if num >= 100 and num <= 999:
        n = str(num)
        s = 0
        for i in n:
            s += int(i)
        return s
    else:
        return -1