def calcula_estado(alunos):
    estado = []
    for i in range(len(alunos)):
        nome = alunos[i][0]
        
        #QUIZZES
        quizzes = alunos[i][1]
        medquizzes = (sum(quizzes) - min(quizzes))/4

        #AF e AI
        AI = alunos[i][2][0]
        AF = alunos[i][2][1]

        media_final = 0.1*medquizzes + 0.4*AI + 0.5*AF

        if media_final >= 5: 
            estado.append([nome, 'A'])
        else:
            estado.append([nome, 'R'])
    return estado