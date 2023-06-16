def notas_dp(lnotas):
    dp = []
    for aluno in lnotas:
        media = (aluno['PI'] + aluno['PF'])/2
        if media < 5:
            dp.append(aluno['matricula'])
    return dp