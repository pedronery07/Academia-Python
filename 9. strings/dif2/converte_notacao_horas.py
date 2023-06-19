# Formato 24h para formato 12h
def converteHora(horas):
    if int(horas[:2]) <= 12:
        if int(horas[:2]) != 12:
            horas += " AM"
        else:
            horas += " PM"
        return horas
    else:
        correcao = horas.replace(horas[:2], "0" + str(int(horas[:2]) - 12))
        correcao += " PM"
    return correcao