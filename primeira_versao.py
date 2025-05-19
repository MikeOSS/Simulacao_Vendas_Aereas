# Simulação da vendas aéreas.
#   Data de Entrega: 13/04/2025

# Membros:
#   . Gustavo Antônio Mariano
#   . João Paulo Ferreira
#   . Leonardo Gambaroni ALves
#   . Miguel Fernandes Costacurta
#   . Max Thomazini Barbosa

import os

info_voo = []
voos = {}
fim = 1
# funções:


def cadastro_voo():

    # Tela de Cadastro do Voo
    print("=============================================================")
    print("                   Bem Vindo ao Cadastro                     ")
    print("                           do Voo                            ")
    print("=============================================================")

    codigo = int(input("Digite o número do Voo: "))

    while codigo in voos:

        os.system('cls' if os.name == 'nt' else 'clear')

        print("==========================================")
        print("              VOO JÁ EXISTE               ")
        print("            Digite um novo Voo            ")
        print("==========================================")
        codigo = int(input("Digite o número do Voo: "))

    origem = input("Digite a origem do Voo: ")
    destino = input("Digite o destino do Voo: ")
    numEscala = int(input("Digite a quantidade de escalas do Voo: "))
    preco = float(input("Digite o preço da passagem: "))

    os.system('cls' if os.name == 'nt' else 'clear')

    info_voo.append(origem)
    info_voo.append(destino)
    info_voo.append(numEscala)
    info_voo.append(preco)

    voos[codigo] = info_voo


def consulta_voo():
    print('==============================================================')
    print('                 COMO DESEJA CONSULTAR O VOO?                 ')
    print('1. Pelo Código.                                               ')
    print('2. Pela cidade de origem.                                     ')
    print('3. Pela cidade de destino.                                    ')
    opcao = int(input('Digite a opção que você deseja (1 - 3): '))
    os.system('cls' if os.name == 'nt' else 'clear')

    while opcao < 1 or opcao > 3:
        print("==========================================")
        print("             VALOR INVÁLIDO               ")
        print("       Digite um número entre 1 e 3       ")
        print("==========================================")
        opcao = int(input('Digite a opção que você deseja (1 - 3): '))
        os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        codigo_voo = int(input('Digite o número do voo: '))
        
        while codigo_voo not in voos.keys():
            print("==========================================")
            print("             VOO NÃO EXISTE               ")
            print("       Digite um número de outro Voo      ")
            print("==========================================")
            
            codigo_voo = int(input("Digite o número do voo: "))

        if codigo_voo in voos.keys():
            print(f'''Número do voo: {codigo_voo} \nCidade de origem:
            {voos[codigo_voo][0]} \nCidade de destino: {voos[codigo_voo][1]}
            \nQuantidade de escalas: {voos[codigo_voo][2]} \nPreço passagem: 
            {voos[codigo_voo][3]}''')

        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == 2:
            cidade_org = input('Digite a cidade de origem do voo: ')
            
            for codigo, infos in voos.items():
                while cidade_org not in infos:
                    print("==========================================")
                    print("             VOO NÃO EXISTE               ")
                    print("       Digite outra cidade de origem      ")
                    print("==========================================")
                    cidade_org = input("Digite a cidade de origem do voo: ")
            
                if cidade_org in infos[0]:
                    print(f'''Número do voo: {codigo} \nCidade de origem:
                    {voos[codigo][0]} \nCidade de destino: {voos[codigo][1]}
                    \nQuantidade de escalas: {voos[codigo][2]} \nPreço passagem: 
                    {voos[codigo][3]}''')
            
            
    

# #def escala_menor(): 
#     menor = 100000
#     #for i in voos.values():
        

while fim == 1:

    print("==============================================================")
    print(f"                    MENU DAS VENDAS AEREAS                   ")
    print("                           SIMULACAO                          ")
    print("\n                      ESCOLHA UMA OPÇÃO                   \n")
    print("1. Cadastro do Voo.")
    print("2. Consultar Voo.")
    print("3. Verificar Voo com Menor Escala.")
    print("4. Listar os passageiros do Voo.")
    print("5. Venda de Passagem.")
    print("6. Cancelamento de Passagem.")
    print("7. Fim.")
    print("==============================================================\n")

    opcao = int(input("Digite a opção que você deseja (1-7): "))
    os.system('cls' if os.name == 'nt' else 'clear')

    while opcao < 1 or opcao > 7:

        print("==========================================")
        print("             VALOR INVÁLIDO               ")
        print("       Digite um número entre 1 e 7       ")
        print("==========================================")
        print("\n          ESCOLHA UMA OPÇÃO           \n")
        print("1. Cadastro do Voo.")
        print("2. Consultar Voo.")
        print("3. Verificar Voo com Menor Escala.")
        print("4. Listar os passageiros do Voo.")
        print("5. Venda de Passagem.")
        print("6. Cancelamento de Passagem.")
        print("7. Fim.")
        print("==========================================")

        opcao = int(input("Digite a opção que você deseja (1-7): "))
        os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        cadastro_voo()
    if opcao == 2:
        consulta_voo()

    elif opcao == 7:
        fim = 0
        

    