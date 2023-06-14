from math import factorial
def calcula_serie(n):
    fact = 2
    num = 2
    expo = 2
    conta = 0 
    if n == 1:
        return 1/(5*3)
    while fact <= n:
        conta += (num*factorial(fact))/(5*(3**expo))
        fact += 1
        num *= 2
        expo += 1
    return (conta + (1/(5*3)))