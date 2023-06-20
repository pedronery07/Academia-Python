def eh_primo(n):
    i = 1
    a = 0
    if n < 0:
        return False
    while i <= n + 1:
        if n == 0 or n == 1:
            i = 1
            return False
        if n % i == 0:
            a += 1
            i += 1
        else:
            i += 1
    if a > 2:
        return False
    else:
        return True

def primos_entre(a, b):
    i = a
    l = []
    while i <= b:
        num = eh_primo(i)
        if num == True:
            l.append(i)
        i += 1
    return l