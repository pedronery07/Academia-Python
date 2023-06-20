#Maiúscula e minúsculas consideradas diferentes
def apaga_repetidos(texto):
    registro = []
    txt_com_ast = ''
    for letra in texto:
        if letra not in registro:
            registro.append(letra)
            txt_com_ast += letra
        else:
            txt_com_ast += '*'
    return txt_com_ast 

# Maiúsculas e minúsculas consideradas iguais
def apaga_repetidos(texto):
   registro = []
   txt_com_ast = ''
   for letra in texto:
       if letra.lower() not in registro or letra.upper() not in registro:
           registro.append(letra.lower())
           registro.append(letra.upper())
           txt_com_ast += letra
       else:
           txt_com_ast += '*'
   return txt_com_ast