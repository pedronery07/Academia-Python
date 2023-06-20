def dias_do_ano(data):
    lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = int(data[0] + data[1])
    mes = int(data[3] + data[4])
    i = 1
    dias = 0
    while i < mes:
        dias += lista[i-1]
        i += 1
    dias += dia
    return dias - 1