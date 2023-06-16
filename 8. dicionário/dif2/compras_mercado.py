def valor_a_devolver(prat, caixa, lcompras):
    saida = 0
    for compra in lcompras:
        #Percorre lista de compras
        prod = compra[0]
        marca = compra[1]
        qtde = compra[2]
        #Verifica valor nas prateleiras
        marcas_prat = prat[prod]
        valor_prat = marcas_prat[marca]
        #Verifica valor no caixa
        marcas_caixa = caixa[prod]
        valor_caixa = marcas_caixa[marca]
        if valor_prat < valor_caixa:
            saida += valor_caixa*qtde - valor_prat*qtde
    return saida