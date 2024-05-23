import datetime
data = datetime.datetime.now()
data_formatada = data.strftime("%d/%m/%y")
hora_formatada = data.strftime("%H:%M")


while True:
    print("O que você deseja assistir hoje?")
    print("[1] - Hora Atual")
    print("[2] - Ação")
    print("[3] - Comédia")
    print("[4] - Terror")
    print("[5] - Romance")
    print("[6] - Suspense")
    print("[7] - Drama")
    print("[8] - Ficcao Cientifica")
    print("[9] - Aventura")
    print("[10] - Musical")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f" A data de hoje é: {data_formatada, hora_formatada}")
    elif  opcao == "2":
        print("Os filmes Vingadores e 007 e uma otima opcao")

    if  opcao == "3":
        print("Minha mae e uma peca, As Branquelas e uma otima opcao para quem gosta de dar boas risadas")

    elif opcao == "4":
        print("A Casa de Cera, Panico na Floresta trazem fortes adrenalinas")

    if  opcao == "5":
        print("E assim que acaba, A Barraca do Beijo para casais apaixonados")

    if  opcao == "6":
        print("O mundo depois de nos, 2012 expressam fortes emocoes")

    if  opcao == "7":
        print("Meninas nao choram, Milagres do Paraiso historias baseados em fatos reais")

    if  opcao == "8":
        print("Interestelar, Jurassic Park para quem gosta de experiencia surreal")

    if  opcao == "9":
        print("Jumanji, Alice no Pais das Maravilhas filmes que nos fazem fugir da nossa realidade")

    if  opcao == "10":
        print("Matilda o musical,High School Musical melhora o humor e aumenta a autoestima ")    

       
    elif opcao == "Sair":
        print("Programa finalizado ")
        break



# opacao = input("O que você deseja")
# romance = "Assim que começa, A barraca do beijo"
# acao = "Doutor Estranho, Os vingadores"


# if opcao == "Filmes de romance":
    # print(f" Essas são boas opções de filmes de romance: {romance}")

# elif opcao == "Filmes para assistir na terça":
    # print(f" Essas são boas opções de filmes para se assistir na terça: {acao}")











