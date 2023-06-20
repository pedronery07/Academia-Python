def eh_respiravel(atm):
    o2 = 0
    total = 0
    for i in range(len(atm)):
        for j in range(len(atm[i])):
            if atm[i][j] == 'O':
                o2 += 1
            total += 1
    if (o2/total)*100 >= 20:
        return True
    else:
        return False 
