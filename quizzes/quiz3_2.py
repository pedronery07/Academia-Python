def busca_restaurantes(l, cat, valor):
    r = []
    for i in range(len(l)):
        if cat == 'culinaria':
            if l[i][1] == valor:
                r.append(l[i][0])
        elif cat == 'ambiente':
            if l[i][2] == valor:
                r.append(l[i][0])
        elif cat == 'preco':
            if l[i][3] <= valor:
                r.append(l[i][0])
    return r