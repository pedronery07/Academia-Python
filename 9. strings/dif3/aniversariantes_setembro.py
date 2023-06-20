def aniversariantes_de_setembro(aniversarios):
    setembristas = {}
    for pessoa, data in aniversarios.items():
        if data[3:5] == '09':
            setembristas[pessoa] = data
    return setembristas