def calcula_frete(valor_total_pedido,q_itens,item_fragil,dist):
    vb = 12.75 
    vkm = 1.82

    if item_fragil == "S" or item_fragil == "s":
        aliquota = 1.75/100
    else:
        aliquota = 0.80/100

    vs = valor_total_pedido*aliquota
    
    if q_itens % 40 == 0:
        q_caixas = q_itens/40
    else:
        q_caixas = q_itens//40 + 1

    frete = vb + q_caixas * vkm * dist + vs
    return frete