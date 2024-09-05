def contador_agua():
    total_agua = 0 
    print("Bem-vindo ao Contador de Água!") 
    print("------------------------------") 

    while True: 
        entrada = input("Digite a quantidade de água bebida (em ml) ou 'SAIR' para encerrar: ") 
        
        if entrada.upper() == 'SAIR': 
            litros = total_agua / 1000 
            print(f"\nTotal de água bebida hoje: {litros:.2f} litros") 
            break 
        
        quantidade = float(entrada)
        
        if quantidade > 0: 
            total_agua += quantidade 
            litros = total_agua / 1000 
            print(f"Total acumulado de água: {litros:.2f} litros") 
        else: 
            print("Por favor, insira uma quantidade positiva.")

    print("Obrigado por usar o contador de água!")

def organizador_treinos():
    treinos = []
    print("Bem-vindo ao Organizador de Treinos!") 
    print("------------------------------") 

    while True:
        acao = input("Digite 'ADICIONAR' para adicionar um treino, 'LISTAR' para listar os treinos ou 'SAIR' para encerrar: ").upper()
        
        if acao == 'SAIR':
            break
        elif acao == 'ADICIONAR':
            treino = input("Digite o treino que você realizou: ")
            treinos.append(treino)
            print("Treino adicionado.")
        elif acao == 'LISTAR':
            print("Treinos registrados:")
            for t in treinos:
                print(f"- {t}")
        else:
            print("Opção inválida. Por favor, escolha 'ADICIONAR', 'LISTAR' ou 'SAIR'.")

    print("Obrigado por usar o organizador de treinos!")

def contador_dias_academia():
    dias = 0
    print("Bem-vindo ao Contador de Dias na Academia!") 
    print("------------------------------") 

    while True:
        acao = input("Digite 'ADICIONAR' para adicionar um dia de treino, 'VER' para ver o total de dias ou 'SAIR' para encerrar: ").upper()
        
        if acao == 'SAIR':
            break
        elif acao == 'ADICIONAR':
            dias += 1
            print("Dia adicionado.")
        elif acao == 'VER':
            print(f"Total de dias na academia: {dias}")
        else:
            print("Opção inválida. Por favor, escolha 'ADICIONAR', 'VER' ou 'SAIR'.")

    print("Obrigado por usar o contador de dias na academia!")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Contador de Água")
        print("2. Organizador de Treinos")
        print("3. Contador de Dias na Academia")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            contador_agua()
        elif escolha == '2':
            organizador_treinos()
        elif escolha == '3':
            contador_dias_academia()
        elif escolha == '4':
            print("Obrigado e até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
