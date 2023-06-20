def calcula_dano(personagem):
    forca_total = personagem['força']
    if personagem['equipamentos'] != []:
        for itens in personagem['equipamentos']:
            forca_total += itens['força']
    return forca_total