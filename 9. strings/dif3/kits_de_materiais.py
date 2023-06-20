def separa_por_inicial(turmas):
    results = {}
    for turma in turmas.values():
        for aluno in turma:
            if aluno[0] not in results.keys():
                results[aluno[0]] = [aluno]
            else:
                results[aluno[0]].append(aluno)
    return results