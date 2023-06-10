def meta_atingida(lrecl, ljust, recl, just):
    if recl < lrecl and just < ljust:
        return True
    else:
        return False