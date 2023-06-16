from math import sqrt
def calcula_tempo(dic_atletas):
    dic_tempos = {}
    for k, v in dic_atletas.items():
        tempo = sqrt((200)/v)
        dic_tempos[k] = tempo
    return dic_tempos

dici_aceleracao = {}
while True:
    nome = str(input('Nome: '))
    if nome == 'sair':
        break
    a = float(input('Aceleração: '))
    dici_aceleracao[nome] = a

dici_tempo = calcula_tempo(dici_aceleracao)

i = 0
for atleta, t in dici_tempo.items():
    if i == 0:
        menor = t
        vencedor = atleta
        i = 1
    elif t < menor:
        vencedor = atleta
        menor = t    

print(f'O vencedor é {vencedor} com tempo de conclusão de {menor} s')