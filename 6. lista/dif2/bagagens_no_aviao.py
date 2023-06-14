def filtra_bagagens(bagagens, hlim, larglim, proflim):
    contador = 0
    for i in range(len(bagagens)):
        if bagagens[i][0] > hlim or bagagens[i][1] > larglim or bagagens[i][2] > proflim:
            contador += 1
    return contador