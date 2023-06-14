# Valida entradas na calculadora
def valida_entradas(l):
    operadores = '+-*/**//%'
    if len(l) == 1:
        return False
    elif l == []:
        return False
    i = 1
    if len(l) != 2:
        while i < len(l):
            if i == len(l)-2 or i == len(l)-1:
                if l[i] != "=":
                    return False
            elif l[i] not in operadores:
                return False
            i += 2
    if l[len(l)-1] == "=":
        return True
    else:
        return False