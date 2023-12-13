# Declarando Constantes
LIMITE_VALOR = 500
LIMITE_SAQUE = 3

# Declarando as Variáveis
menu = '''
>>> Digite a Opção Desejada <<<
(d) Depósito
(s) Saque
(e) Extrato
(q) Sair
'''
Quantidade_Saques = 0
saldo = 0.0
depositos = 0.0
saques = 0.0
extrato = ''

# Sistema
while True:
    opcao = input(menu)
    # Operação de Depósito
    if opcao == 'd':
        valor_deposito = float(input('Informe o valor para Depósito. '))
        if valor_deposito < 0:
            print('Valor inserido é inválido. Refaça a operação!')
        else:
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
            saldo += valor_deposito
    # Operação de Saque
    elif opcao == 's':
        if Quantidade_Saques < LIMITE_SAQUE:
            valor_saque = float(input('Informe o valor de saque. '))
            if valor_saque < 0:
                print('Valor inserido é inválido. Refaça a operação!')
            elif valor_saque > LIMITE_VALOR:
                print('Valor superior ao seu limite diário.')
            elif valor_saque > saldo:
                print('Saldo insuficiente.')
            else:
                extrato += f'Saque: R$ {valor_saque*-1:.2f}\n'
                saldo -= valor_saque
                Quantidade_Saques += 1
        else:
            print('Quantidade de saques diários excedido.')
    # Operação de Extrato
    elif opcao == 'e':
        print('\n>>>>>> EXTRATO BANCÁRIO <<<<<<')
        print('Não existem movimentações a serem mostradas.' if not extrato else extrato)
        print(f'Saldo R$ {saldo:.2f}')
        print('\n>>>>>>> fim do Extrado <<<<<<<')

    elif opcao == 'q':
        break
    else:
        print("Opção inválida, encerrando atendimento.")
