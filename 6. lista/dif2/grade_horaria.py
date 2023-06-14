def compromisso_no_periodo(grade, dia, periodo):
    for i in range(len(grade)):
        if i == periodo:
            if grade[i][dia] == '':
                return 'Livre'
            else:
                return grade[i][dia] 