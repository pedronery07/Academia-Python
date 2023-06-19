def classifica_rima(sil1, sil2, sil3, sil4):
    if sil1 == sil2 == sil3 == sil4:
        return 'outra'
    elif sil1 == sil2 and sil3 == sil4:
        return 'emparelhada'
    elif sil1 == sil3 and sil2 == sil4:
        return 'alternada'
    elif sil1 == sil4 and sil2 == sil3:
        return 'interpolada'
    else:
        return 'outra'