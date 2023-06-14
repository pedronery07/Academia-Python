def nota_quizzes(q1, q2, q3, q4, q5):
    l = [q1, q2, q3, q4, q5]
    if q1 > 10 or q1 < 0:
        return 0
    if q2 > 10 or q2 < 0:
        return 0
    if q3 > 10 or q3 < 0:
        return 0
    if q4 > 10 or q4 < 0:
        return 0
    if q5 > 10 or q5 < 0:
        return 0
    descarte = min(l)
    media = (sum(l) - descarte)/4
    return media

def nota_final(medq, AI, AF, EP1, EP2, PF):
    if medq < 0 or AI < 0 or AF < 0 or EP1 < 0 or EP2 < 0 or PF < 0:
        return 0
    elif medq > 10 or AI > 10 or AF > 10 or EP1 > 10 or EP2 > 10 or PF > 10:
        return 0
    ni = 0.4*AI + 0.5*AF + 0.1*medq
    ng = 0.1*EP1 + 0.2*EP2 + 0.7*PF
    if ni >= 5 and ng >= 5:
        nf = (ni + ng)/2
    else:
        nf = min(ni, ng)
    return nf

soma = 0
n = 0
aprovados = 0
reprovados = 0
i = 1

while True:
    add_notas = str(input("Você deseja adicionar notas de mais um aluno?"))
    if add_notas != 'não':
        i += 1
        q1 = int(input("Nota quiz 1: "))
        q2 = int(input("Nota quiz 2: "))
        q3 = int(input("Nota quiz 3: "))
        q4 = int(input("Nota quiz 4: "))
        q5 = int(input("Nota quiz 5: "))
        AI = int(input("Nota AI: "))
        AF = int(input("Nota AF: "))
        EP1 = int(input("Nota EP1: "))
        EP2 = int(input("Nota EP2: "))
        PF = int(input("Nota PF: "))
        medq = nota_quizzes(q1, q2, q3, q4, q5)
        nota = nota_final(medq, AI, AF, EP1, EP2, PF)
        if nota < 5:
            reprovados += 1
        else:
            aprovados += 1
        print(f'Nota final do aluno: {nota:.2f}')
        soma += nota
        n += 1
    else:
        break

if i == 1:
    print(f'Média da sala: 0.00')
    print(f'Aprovados: 0.00%')
    print(f'Reprovados: 0.00%')
else:
    medsala = soma/n        
    print(f'Média da sala: {medsala:.2f}')
    print(f'Aprovados: {(aprovados*100)/n:.2f}%')
    print(f'Reprovados: {(reprovados*100)/n:.2f}%')