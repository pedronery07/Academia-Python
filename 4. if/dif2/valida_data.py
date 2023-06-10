def valida_data(d, m, a):
    l31 = [1,3,5,7,8,10,12]
    l30 = [4,6,9,11]
    if m == 2:
        if 0 < d <= 28:
            return True
        elif d == 29:
            if a % 4 == 0 and a % 400 == 0:
                return True
            elif a % 4 != 0:
                return False
            elif a % 4 == 0 and a % 100 == 0 and a % 400 != 0:
                return False
            else:
                return True
    if 0 < d <= 31 and m in l31:
        return True
    elif 0 < d <= 30 and m in l30:
        return True