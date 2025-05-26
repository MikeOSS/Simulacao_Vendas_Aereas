# Simulação da vendas aéreas.
#   Data de Entrega: 13/04/2025

# Membros:
#   . Gustavo Antônio Mariano
#   . João Paulo Ferreira
#   . Leonardo Gambaroni ALves
#   . Miguel Fernandes Costacurta
#   . Max Thomazini Barbosa

import os


voos = {}
passageiros_dos_voos = {}
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

    info_voo = [origem, destino, numEscala, preco]

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
            print("      Digite outro codigo de viagem       ")
            print("==========================================")

            codigo_voo = int(input("Digite o número do voo: "))
            os.system('cls' if os.name == 'nt' else 'clear')

        if codigo_voo in voos.keys():
            print("==========================================")
            print("           Informações do Voo             ")
            print("==========================================")
            print(f'''
            Número do voo: {codigo_voo} 
            Cidade de origem:{voos[codigo_voo][0]} 
            Cidade de destino:{voos[codigo_voo][1]}
            Quantidade de escalas:{voos[codigo_voo][2]}
            Preço passagem: {voos[codigo_voo][3]}''')

        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == 2:
        cidade_org = input('Digite a cidade de origem do voo: ')
        cidade_org_cadastrada = []

        for codigo, infos in voos.items():
            cidade_org_cadastrada.append(voos[codigo][0])

        while cidade_org not in cidade_org_cadastrada:
            print("==========================================")
            print("             VOO NÃO EXISTE               ")
            print("       Digite outra cidade de origem      ")
            print("==========================================")
            cidade_org = input("Digite a cidade de origem do voo: ")
            os.system('cls' if os.name == 'nt' else 'clear')

        for codigo, infos in voos.items():
            if infos[0] == cidade_org:
                print("==========================================")
                print("           Informações do Voo             ")
                print("==========================================")
                print(f'''
                    Número do voo: {codigo}
                    Cidade de origem: {infos[0]}
                    Cidade de destino: {infos[1]}
                    Quantidade de escalas: {infos[2]}
                        Preço passagem: {infos[3]}''')    

        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == 3:
        cidade_dest = input('Digite a cidade de origem do voo: ')
        cidade_dest_cadastrada = []

        for codigo, infos in voos.items():
            cidade_dest_cadastrada.append(voos[codigo][1])

        while cidade_dest not in cidade_dest_cadastrada:
            print("==========================================")
            print("             VOO NÃO EXISTE               ")
            print("       Digite outra cidade de origem      ")
            print("==========================================")
            cidade_dest = input("Digite a cidade de origem do voo: ")
            os.system('cls' if os.name == 'nt' else 'clear')

        for codigo, infos in voos.items():
            if infos[1] == cidade_dest:
                print("==========================================")
                print("           Informações do Voo             ")
                print("==========================================")
                print(f'''
                    Número do voo: {codigo}
                    Cidade de origem: {infos[0]}
                    Cidade de destino: {infos[1]}
                    Quantidade de escalas: {infos[2]}
                        Preço passagem: {infos[3]}''')    

        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')

def escala_menor():
    menor_escala = 9999999
    if not voos:
        print("não possui voos")
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        for id_voo, inf_voo in voos.items():
            escala_atual = inf_voo[2]
            if escala_atual < menor_escala:
                menor_escala = escala_atual
        for codigo, informacoes in voos.items():
            if menor_escala == informacoes[2]:
                print(f'''
                Número do voo: {codigo} 
                Cidade de origem:{voos[codigo][0]} 
                Cidade de destino:{voos[codigo][1]}
                Quantidade de escalas:{voos[codigo][2]}
                Preço passagem: {voos[codigo][3]}''')
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')


def venda_passagem():
    # cadastro do passageiro:
    print("==============================================================")
    print(f"                     Seja muito bem vindo!                   ")
    print("                       Informe seus dados:                    ")
    nome = input('Digite seu nome: ')
    cpf = int(input('Digite seu cpf: '))
    origem = input('Digite sua cidade de origem: ')
    destino = input('Digite seu destino: ')
    for codigo, infos in voos.items():
        # adicionar um or caso o voo esteja cheio posteriormente

        if destino != infos[1] and origem != infos[0]:
            print("==========================================")
            print("             NÃO TEMOS PASSAGENS          ")
            print("          COM TAIS ORIGEM E DESTINO       ")
        else:
            while destino.lower() != infos[1].lower():
                print("==========================================")
                print("             NÃO TEMOS PASSAGENS          ")
                print("              PARA ESSE DESTINO           ")
                print("1. Selecionar outro destino ")
                print("2. Sair                     ")
                print("==========================================")
                opcao = int(input('Digite sua opção: '))
                while opcao < 1 or opcao > 2:
                    opcao = int(input('Digite sua opção: '))
                if opcao == 1:
                    destino = input('Digite seu destino: ')
                    if origem in infos[0] and destino in infos[1]:
                        print(
                            f'Voo número {codigo} saindo de {infos[0]} com destino para {infos[1]} existe!')
                        escolha = input(
                            f'Deseja comprar a passagem no valor de: R$ {infos[3]} ? (S ou N): ')
                        if escolha.lower() == 's':
                            passageiros = []
                            passageiros.append(nome)
                            passageiros.append(cpf)
                            passageiros.append(origem)
                            passageiros.append(destino)
                            if codigo not in passageiros_dos_voos:
                                passageiros_dos_voos[codigo] = []
                            passageiros_dos_voos[codigo].append(passageiros)
                        else:
                            print('Ok! Redirecionando para a tela principal: ')
                            input('<<Tecle qualquer coisa >>')
                else:
                    break

            while origem.lower() != infos[0].lower():
                print("==========================================")
                print("             NÃO TEMOS PASSAGENS          ")
                print("             SAINDO DE SUA CIDADE         ")
                print("==========================================")
                input('<<Tecle qualquer coisa>>')
                break

            if origem in infos[0] and destino in infos[1]:
                print(
                    f'Voo número {codigo} saindo de {infos[0]} com destino para {infos[1]} existe!')
                escolha = input(
                    f'Deseja comprar a passagem no valor de: R$ {infos[3]} ? (S ou N): ')
                if escolha.lower() == 's':
                    print("==========================================")
                    print("        COMPRA EFETUADA COM SUCESSO!      ")
                    print("==========================================")
                    passageiros = []
                    passageiros.append(nome)
                    passageiros.append(cpf)
                    passageiros.append(origem)
                    passageiros.append(destino)
                    if codigo not in passageiros_dos_voos:
                        passageiros_dos_voos[codigo] = []
                    passageiros_dos_voos[codigo].append(passageiros)
                else:
                    print('Ok! Redirecionando para a tela principal: ')
                    input('<<Tecle qualquer coisa >>')


def listar_passageiros():
    print("==========================================")
    print("          LISTAGEM DE PASSAGEIROS         ")
    print("==========================================")
    listar = int(input('Digite o código do voo: '))

    while listar not in passageiros_dos_voos.keys():
        print("==========================================")
        print("             VOO NÃO EXISTE               ")
        print("==========================================")
        listar = int(input('Digite outro código do voo: '))

    else:
        for i in passageiros_dos_voos[listar]:
            print(f'''
            Nome:    {i[0]}
            CPF:     {i[1]}
            Origem:  {i[2]}
            Destino: {i[3]}
            ''')


def cancelamento_passagem():
    print("==========================================")
    print("        CANCELAMENTO DE PASSAGEM          ")
    print("==========================================")
    excluir = int(input('Digite o seu cpf: '))
    for codigo, infos in passageiros_dos_voos.items():
        for i in infos:
            if excluir == i[1]:
                print("====================================================")
                print(" ATENÇÃO: DESEJA MESMO CANCELAR A PASSAGEM? ")
                print("====================================================")
                escolha = input('Digite sim ou não: ')
                if escolha.lower() == 'sim':
                    infos.remove(i)
                    print('PASSAGEIRO REMOVIDO COM SUCESSO!!')
                else:
                    print('OPERAÇÃO CANCELADA!')


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
    if opcao == 3:
        escala_menor()
    if opcao == 4:
        listar_passageiros()
    if opcao == 5:
        venda_passagem()
    if opcao == 6:
        cancelamento_passagem()

    elif opcao == 7:
        fim = 0
