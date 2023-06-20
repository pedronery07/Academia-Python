def converte_receita(receita):
    correção = {}
    conversão = {
        'xícara': 250,
        'xícaras': 250,
        'colher de sopa': 15,
        'colheres de sopa': 15,
        'colher de chá': 5,
        'colheres de chá': 5
    }
    for ing, qtde in receita.items():
        confere = qtde.split()
        if ' ' in qtde:
            qtd = int(confere[0])
            sem_num = qtde[2:]
            correção[ing] = str(conversão[sem_num]*qtd) + ' ml'
        else:
            correção[ing] = qtde
    return correção