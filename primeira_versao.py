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
    limite_passageiros = int(
        input("Digite o limite de passageiros para este Voo: "))

    os.system('cls' if os.name == 'nt' else 'clear')

<<<<<<< Updated upstream
    info_voo.append(origem)
    info_voo.append(destino)
    info_voo.append(numEscala)
    info_voo.append(preco)
=======
    info_voo = [origem, destino, numEscala, preco, limite_passageiros]
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        
        for codigo_voo in voos.keys():
            while codigo_voo not in voos.keys():
                print("==========================================")
                print("             VOO NÃO EXISTE               ")
                print("      Digite outro codigo de viagem       ")
                print("==========================================")
                Codigo_voo = int(input("Digite a cidade de origem do voo: "))
            
            if codigo_voo in voos.keys():
               print(f'''Número do voo: {codigo_voo} 
                Cidade de origem:{voos[codigo_voo][0]} 
                Cidade de destino:{voos[codigo_voo][1]}
                Quantidade de escalas:{voos[codigo_voo][2]}
                Preço passagem: {voos[codigo_voo][3]}''')
                    
=======

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
            Cidade de origem: {voos[codigo_voo][0]} 
            Cidade de destino: {voos[codigo_voo][1]}
            Quantidade de escalas: {voos[codigo_voo][2]}
                Preço passagem: {voos[codigo_voo][3]}''')

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                cidade_org = input("Digite a cidade de origem do voo: ")
            
            if cidade_org in infos[0]:
                print(f'''Número do voo: {codigo} 
                Cidade de origem:{voos[codigo][0]} 
                Cidade de destino:{voos[codigo][1]}
                Quantidade de escalas:{voos[codigo][2]}
                Preço passagem: {voos[codigo][3]}''')
               
=======
                print(f'''
                Número do voo: {codigo}
                Cidade de origem: {infos[0]}
                Cidade de destino: {infos[1]}
                Quantidade de escalas: {infos[2]}
                    Preço passagem: {infos[3]}''')

        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcao == 3:
        cidade_dest = input('Digite a cidade de destino do voo: ')
        cidade_dest_cadastrada = []

        for codigo, infos in voos.items():
            cidade_dest_cadastrada.append(voos[codigo][1])

        while cidade_dest not in cidade_dest_cadastrada:
            print("==========================================")
            print("             VOO NÃO EXISTE               ")
            print("       Digite outra cidade de destino     ")
            print("==========================================")
            cidade_dest = input("Digite a cidade de destino do voo: ")
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
        for inf_voo in voos.values():
            escala_atual = inf_voo[2]
            if escala_atual < menor_escala:
                menor_escala = escala_atual
        for codigo, informacoes in voos.items():
            if menor_escala == informacoes[2]:
                print("==========================================")
                print("           Voo com menor escala           ")
                print("==========================================")
                print(f'''
                Número do voo: {codigo} 
                Cidade de origem: {voos[codigo][0]} 
                Cidade de destino: {voos[codigo][1]}
                Quantidade de escalas: {voos[codigo][2]}
                    Preço passagem: {voos[codigo][3]}''')

>>>>>>> Stashed changes
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')


    elif opcao == 3:
        cidade_dest = input('Digite a cidade de origem do voo: ')
            
        for codigo, infos in voos.items():
            while cidade_dest not in infos:
                print("==========================================")
                print("             VOO NÃO EXISTE               ")
                print("       Digite outra cidade de origem      ")
                print("==========================================")
<<<<<<< Updated upstream
                cidade_dest = input("Digite a cidade de origem do voo: ")
            
            if cidade_dest in infos[1]:
                print(f'''Número do voo: {codigo} 
                Cidade de origem:{voos[codigo][0]} 
                Cidade de destino:{voos[codigo][1]}
                Quantidade de escalas:{voos[codigo][2]}
                Preço passagem: {voos[codigo][3]}''')
                    
        input('\n\t<< Tecle Enter para continuar >>')
        os.system('cls' if os.name == 'nt' else 'clear')
            
            
    
=======
                opcao = int(input('Digite sua opção: '))
                while opcao < 1 or opcao > 2:
                    opcao = int(input('Digite sua opção: '))
                if opcao == 1:
                    destino = input('Digite seu destino: ')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

            if origem.lower() != infos[0].lower():
                print("==========================================")
                print("             NÃO TEMOS PASSAGENS          ")
                print("             SAINDO DE SUA CIDADE         ")
                print("==========================================")
                input('\n\t<< Tecle Enter para continuar >>')
                os.system('cls' if os.name == 'nt' else 'clear')

            if origem in infos[0] and destino in infos[1]:
                limite_voo = infos[4]
                passageiros_no_voo_atual = 0
                if codigo in passageiros_dos_voos:
                    passageiros_no_voo_atual = len(
                        passageiros_dos_voos[codigo])
                if passageiros_no_voo_atual < limite_voo:
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
                        input('\n\t<< Tecle Enter para continuar >>')
                        os.system('cls' if os.name == 'nt' else 'clear')

                    else:
                        print('Ok! Redirecionando para a tela principal: ')
                        input('\n\t<< Tecle Enter para continuar >>')
                        os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("==========================================")
                    print("              VOO LOTADO!!!               ")
                    print("==========================================")


def listar_passageiros():
    print("==========================================")
    print("          LISTAGEM DE PASSAGEIROS         ")
    print("==========================================")
    listar = int(input('Digite o código do voo: '))

    while listar not in passageiros_dos_voos.keys():
        print("==========================================")
        print("             VOO NÃO EXISTE               ")
        print("==========================================")
        print("1. Selecionar outro destino               ")
        print("2. Sair                                   ")
        print("==========================================")
        opcao = int(input('Digite sua opção: '))
        while opcao < 1 or opcao > 2:
            opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            listar = int(input('Digite outro código do voo: '))
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    else:
        for i in passageiros_dos_voos[listar]:
            print(f'''
            Nome:    {i[0]}
            CPF:     {i[1]}
            Origem:  {i[2]}
            Destino: {i[3]}
            ''')
    input('\n\t<< Tecle Enter para continuar >>')
    os.system('cls' if os.name == 'nt' else 'clear')


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
>>>>>>> Stashed changes

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
        

    