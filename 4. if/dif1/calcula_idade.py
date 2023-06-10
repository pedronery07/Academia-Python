def calcula_idade(d_nasc,m_nasc,a_nasc, d_atual, m_atual, a_atual):
    idade = a_atual - a_nasc
    if m_atual < m_nasc:
        return idade - 1
    elif m_atual == m_nasc:
        if d_nasc > d_atual:
            return idade -1 
    return idade