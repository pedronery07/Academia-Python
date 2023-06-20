from math import sqrt

def caminho_mais_curto(caminhos):
    for j in range(len(caminhos)):
        caminho = caminhos[j]
        total = 0
        for i in range(len(caminho)-1):
            x1 = caminho[i][0]
            y1 = caminho[i][1]
            x2 = caminho[i+1][0] 
            y2 = caminho[i+1][1]
            d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
            total += d
        if j == 0:
            menor = total
            menor_caminho = caminho
        if total < menor:
            menor = total
            menor_caminho = caminho
    return menor_caminho