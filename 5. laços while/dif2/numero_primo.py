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