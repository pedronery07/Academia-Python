def nomes_com_vogais(nomes):
    vogais = 'AEIOU'
    conta_vogais = 0
    conta_outras = 0
    for n in nomes:
        if n[0] in vogais:
            conta_vogais += 1
        else:
            conta_outras += 1
    return [conta_vogais, conta_outras]