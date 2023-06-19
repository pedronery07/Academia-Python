def remove_vogais(string):
    sem_vogais = ''
    vogais = 'aeiou'
    for letra in string:
        if letra not in vogais:
            sem_vogais += letra
    return sem_vogais