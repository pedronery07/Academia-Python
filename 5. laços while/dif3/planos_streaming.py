plano = str(input("Qual o seu plano?"))

while True:
    serie = str(input("Qual serie quer assistir?"))
    if serie == "sair":
        print("Ok, tchau!")
        break
    elif serie == "stranger things":
        if plano == "novo":
            print("Precisa comprar novo plano!")    
        else:
            print("Ok, reproduzindo!")
    elif serie == "friends":
        if plano == "novo":
            print("Precisa comprar novo plano!")
        else:
            print("Ok, reproduzindo!")
    elif serie == "the circle":
        if plano == "novo":
            print("Ok, reproduzindo!")
            print("Num oferecimento de DesSoft!")
        else:
            print("Ok, reproduzindo!")
    elif serie == "mad men":
        if plano == "novo":
            print("Ok, reproduzindo!")
            print("Num oferecimento de DesSoft!")
        else:
            print("Ok, reproduzindo!")    
    elif serie == "champions":
        if plano == "novo" or plano == "padrao":
            print("Precisa comprar novo plano!")
        else:
            print("Ok, reproduzindo!")
    elif serie == "brasileirao":
        if plano == "novo" or plano == "padrao":
            print("Precisa comprar novo plano!")
        else:
            print("Ok, reproduzindo!")
    else:
        print("Serie inexistente!")