from math import sqrt
def calcula_tempo(dic_atletas):
    dic_tempos = {}
    for k, v in dic_atletas.items():
        tempo = sqrt((200)/v)
        dic_tempos[k] = tempo
    return dic_tempos
