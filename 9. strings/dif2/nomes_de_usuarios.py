def extrai_nome(email):
    name = ''
    for letra in email:
        if letra == "@":
            return name
        else:
            name += letra
            
def extrai_nomes_de_usuarios(emails_list):
    n = []
    for email in emails_list:
        nome = extrai_nome(email)
        n.append(nome) 
    return n