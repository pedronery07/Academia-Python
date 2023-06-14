def eh_fibonacci(l):
    if len(l) < 3:
        return False
    for i in range(len(l)-2):
        t1 = l[i]
        t2 = l[i+1]
        if l[i+2] != t1 + t2:
            return False
    return True