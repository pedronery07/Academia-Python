def calcula_overbooking(cap, qtde_pass):
    if qtde_pass == []:
        return 0
    contador = 0
    for i in range(len(qtde_pass)):
        if qtde_pass[i] > cap:
            contador += qtde_pass[i] - cap 
    return contador