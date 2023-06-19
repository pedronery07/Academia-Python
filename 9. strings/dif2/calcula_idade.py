def calcula_idade_int(d_nasc,m_nasc,a_nasc, d_atual, m_atual, a_atual):
    idade = a_atual - a_nasc
    if m_atual < m_nasc:
        return idade - 1
    elif m_atual == m_nasc:
        if d_nasc > d_atual:
            return idade -1 
    return idade

def calcula_idade(nascimento, atual):
    ano_atual = int(atual[6:])
    ano_nasc = int(nascimento[6:])
    mes_atual = int(atual[3:5])
    mes_nasc = int(nascimento[3:5])
    dia_atual = int(atual[0:2])
    dia_nasc = int(nascimento[0:2])
    age = calcula_idade_int(dia_nasc, mes_nasc, ano_nasc, dia_atual, mes_atual, ano_atual)
    return age