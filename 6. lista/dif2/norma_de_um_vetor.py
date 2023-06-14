from math import sqrt
def calcula_norma(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += (vetor[i])**2
    return sqrt(soma)