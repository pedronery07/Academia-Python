def valida_senha(senha):
    conta_especiais = 0
    especiais = "#&*%@!?$"
    checador = []
    for letra in senha:
        if letra in especiais and letra not in checador:
            checador.append(letra)
            conta_especiais += 1
    for i in range(len(senha)-1):
        if senha[i+1] == senha[i]:
            return False
    if len(senha) >= 8 and conta_especiais >= 2:
        return True