#USANDO WHILE
#def fatorial(n):
#    i = 1
#    f = 1
#    while i < n:
#        f *= i 
#        i += 1
#    return f

#USANDO FOR
def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f