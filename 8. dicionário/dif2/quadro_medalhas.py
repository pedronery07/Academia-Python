def pais_campeao(quadro_medalhas):
    camp = ""
    for k, v in quadro_medalhas.items():
        if camp == "":
            camp = k
        else:
            if quadro_medalhas[k]['ouro'] > quadro_medalhas[camp]['ouro']:
                camp = k
            elif quadro_medalhas[k]['ouro'] == quadro_medalhas[camp]['ouro']:
                if quadro_medalhas[k]['prata'] > quadro_medalhas[camp]['prata']:
                    camp = k
                elif quadro_medalhas[k]['prata'] == quadro_medalhas[camp]['prata']:
                    if quadro_medalhas[k]['bronze'] > quadro_medalhas[camp]['bronze']:
                        camp = k
    return camp
                