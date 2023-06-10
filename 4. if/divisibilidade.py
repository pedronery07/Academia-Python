def divisivel(n):
    if n % 2 == 0 and n % 3 == 0:
        return 'Insper'
    elif n % 2 == 0:
        return 'Ins'
    elif n % 3 == 0:
        return 'per'
    else:
        return n