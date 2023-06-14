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

def maior_primo_menor_que(n):
    if n < 0:
        return -1
    num = n
    while True:
        eh = eh_primo(num)
        if eh == True:
            return num
        elif num == 0:
            return -1
        num -= 1