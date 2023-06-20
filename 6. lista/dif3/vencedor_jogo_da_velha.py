def verifica_jogo_da_velha(tabuleiro):
    #Horizontais
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2]:
            return tabuleiro[i][0]
    
    #Verticais
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        return tabuleiro[0][0]
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        return tabuleiro[0][1]
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        return tabuleiro[0][2]
    
    #Diagonal 1
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        return tabuleiro[0][0]
    
    #Diagonal 2
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return tabuleiro[0][2]
    
    #Velha
    else:
        return 'V'