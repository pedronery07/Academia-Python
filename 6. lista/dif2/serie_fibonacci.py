def calcula_fibonacci(n):
    if n == 1:
        return [1]
    l = [1, 1]
    i = 1 
    while i <= n - 2:
        proximo = l[i] + l[i-1]
        l.append(proximo)
        i += 1
    return l