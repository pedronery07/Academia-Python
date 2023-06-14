def meta_atingida(lrecl, ljust, recl, just):
    if recl < lrecl and just < ljust:
        return True
    else:
        return False

def classifica_pedido(valor, dias, tam, avaria, capital):
    if valor <= 1000:
        if dias <= 1:
            if valor <= 150:
                if avaria.lower() == 'n':
                    return 'normal'
                else:
                    return 'reclamacao'
            else:
                return 'reclamacao'
        else:
            return 'reclamacao'
    else:
        if dias <= 10:
            if avaria.lower() == 'n':
                if valor <= 10000:
                    if valor <= 5000:
                        if capital.lower() == 'n':
                            return 'normal'
                        else:
                            if tam.lower() == 'p':
                                return 'reclamacao'
                            else:
                                return 'normal'
                    else:
                        return 'reclamacao'
                else:
                    return 'justica'
            else:
                return 'justica'
        else:
            return 'justica'

limrecl = float(input('Limite de reclamações: '))
limjust = float(input('Limite pedidos justiça: '))
continua = input('Adicionar dados? (S/N)')

if continua.lower() == 's':
    contarec = 0
    contaj = 0
    contan = 0
    cont = 0
    while continua.lower() != 'n':
        val = float(input('Valor do pedido: '))
        atr = int(input('Dias de atraso: '))
        tamanho = input('Tamanho da entrega: ')
        avr = input('Houve avaria? (S/N)')
        cap = input('É para uma capital? (S/N)')
        c = classifica_pedido(val, atr, tamanho, avr, cap)
        if c == 'justica':
            contaj += 1
        elif c == 'normal':
            contan += 1
        elif c == 'reclamacao':
            contarec += 1
        cont += 1
        print(f'Pedido classificado como {c}')
        continua = input('Mais dados? (S/N)')
    print(f'Pedidos por classificação: {contarec:02} reclamacao, {contan:02} normal, {contaj:02} justica')
    print(f'Pedidos por classificação: {(contarec/cont)*100:05.2f}% reclamacao, {(contan/cont)*100:05.2f}% normal, {(contaj/cont)*100:05.2f}% justica')
    meta = meta_atingida(limrecl, limjust,(contarec/cont), (contaj/cont))
    if meta == True:
        print('Meta atingida!')
    else:
        print('Meta nao atingida!')