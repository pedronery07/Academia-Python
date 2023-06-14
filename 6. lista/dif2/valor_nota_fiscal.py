def calcula_total_da_nota(preco, qtde):
    total = 0
    for i in range(len(preco)):
        p = preco[i]*qtde[i]
        total += p
    return total