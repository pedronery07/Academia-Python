def pet_pode_viajar(pet, limites, passagens):
    peso_pet_total = pet[2] + pet[3]
    altura = pet[4][0]
    largura = pet[4][1]
    prof = pet[4][2]
    dimensoes = [altura, largura, prof]
    atestado = pet[5]
    #Verifica atestado
    if atestado == 'N':
        return False
    #Verifica peso total do pet
    elif limites[1] < peso_pet_total:
        return False
    #Verifica dimensões da caixinha do pet
    for i in range(len(limites[2])):
        if limites[2][i] < dimensoes[i]:
            return False
    qtde_pets = limites[0]
    conta_cabines = 0
    if limites[0] == 0:
        return False
    #Verifica número de cabines no voo
    for lugares in passagens:
        for itens in lugares[1]:
            if itens == 'pet_cabine':
                conta_cabines += 1
    if conta_cabines < qtde_pets:
        return True
    else:
        return False