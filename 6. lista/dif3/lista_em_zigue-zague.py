def lista_em_zigue_zague(lista):
    if lista == [] or len(lista) == 1:
        return True
    elif len(lista) == 2 and lista[0] != lista[1]:
        return True
    elif len(lista) == 2 and lista[0] == lista[1]:
        return False
    for i in range(len(lista)-1):
        if i == 0:
            if lista[0] > lista[1]:
                status = 'menor'
            else:
                status = 'maior'
        elif lista[i+1] > lista[i] and status == 'maior':
            return False
        elif lista[i+1] < lista[i] and status == 'menor':
            return False
        else:
            if status == 'maior':
                status = 'menor'
            else:
                status = 'maior'
            continue
    return True