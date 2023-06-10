cig_por_dia = int(input('Quantos cigarros fuam por dia? '))
anos = int(input('Há quantos anos fuma? '))

def morte(n, tempo):
    t = n * 10 * 365 * tempo
    return t / 1440

perdido = morte(cig_por_dia, anos)
print(perdido)