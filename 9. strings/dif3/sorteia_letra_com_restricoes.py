from random import choice

def sorteia_letra(palavra, restritas):
    for l in restritas:
        if l.upper() not in restritas:
            restritas.append(l.upper())
        elif l.lower() not in restritas:
            restritas.append(l.lower())
    especiais = ['.', ',', '-', ';', ' ']
    conta_nao_restritas = 0
    retorno = ''
    for letra in palavra:
        if letra not in restritas and letra not in especiais:
            conta_nao_restritas += 1
    if conta_nao_restritas != 0:
        while retorno == '':
            escolha = choice(palavra)
            if escolha not in especiais and escolha not in restritas:
                retorno += escolha
                return retorno
    else:
        return retorno