def login_disponivel(login, lista):
    if lista == [] or login not in lista:
        return login
    i = 1
    confere = 0
    while confere == 0:
        num = str(i)
        for log in lista:
            if log == login + num:
                i += 1
                confere = 0
                break
            confere = 1
    return login + num