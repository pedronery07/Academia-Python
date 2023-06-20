def quando_passa(dic_prog, prog):
    passa = {}
    for canal, programacao in dic_prog.items():
        for hora, p in programacao.items():
            if p == prog:
                if hora not in passa.keys():
                    passa[hora] = [canal]
                else:
                    passa[hora].append(canal)
    return passa