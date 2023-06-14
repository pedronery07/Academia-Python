def eh_primo(n):
    if n == 0 or n == 1 or n < 0:
        return False
    elif n == 2:
        return True
    i = 2   
    while i != n:
        if n % i == 0:
            return False
        i += 1
    return True

def primos_entre(a, b):
    p = a
    l = []
    lprimos = []
    while p <= b:
        l.append(p)
        p += 1
    for i in range(len(l)):
        eh = eh_primo(l[i])
        if eh == True:
            lprimos.append(l[i])
    return len(lprimos)