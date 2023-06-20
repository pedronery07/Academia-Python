def decodifica(string, trocas):
    nova_string = ""
    for letra in string:
        if letra in trocas.values():
            for correto, errado in trocas.items():
                if errado == letra:
                    nova_string += correto 
        else:
            nova_string += letra
    return nova_string