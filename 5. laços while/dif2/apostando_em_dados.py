from random import randint

def apostando_em_dados(num_sorte, aposta0, rodadas):
    i = 1
    aposta = aposta0
    while i <= rodadas:
        sorteio = randint(1,6)
        #Primeira correção da aposta
        if i == 0:
            if sorteio == num_sorte:
                aposta += aposta0*(1/3)
            else:
                aposta -= aposta0*(1/6)
        else:
            if sorteio == num_sorte:
                aposta += aposta*(1/3)
            else:
                aposta -= aposta*(1/6) 
        i += 1 
    return aposta