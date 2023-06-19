def remove_vogais(texto):
    vogais = 'aeiouAEIOU'
    sem_vogais = ""
    for letra in texto:
        if letra not in vogais:
            sem_vogais += letra
    return sem_vogais