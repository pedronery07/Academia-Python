def decimal_para_binario(n):
    if n < 0 :
        return "Negativo"
    b = bin(n)
    b_string = str(b)
    return b_string
