def junta_nome_sobrenome(nome, sobrenome):
    l = []
    for i in range(len(nome)):
        string = nome[i] + ' ' + sobrenome[i]
        l.append(string) 
    return l