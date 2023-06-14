def maximo_divisor_comum(m,n):
    i = 1
    if m > n:
        while i <= n:
            if m % i == 0 and n % i == 0:
                num = i
                i += 1
            i += 1
    elif n > m:
        while i <= m:
            if n % i == 0 and m % i == 0:
                num = i
                i += 1
            i += 1
    return num