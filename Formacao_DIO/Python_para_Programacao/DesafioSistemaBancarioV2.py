# Declarando Constantes
LIMITE_VALOR = 500
LIMITE_SAQUE = 3
QT_SAQUES = 0
SALDO = 0.0
DEPOSITOS = 0.0
SAQUES = 0.0
EXTRATO = ''
USUARIOS = []
CONTAS = []
NR_CONTA = 1
# Declarando as funções


def cria_usuario(nome, data_nascimento, cpf, endereco):
    usuario = [nome, data_nascimento, cpf, endereco]
    return usuario


def cria_conta(agencia, numero_conta, usuario):
    conta = [agencia, numero_conta, usuario]
    return conta


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        extrato = f'Depósito: R$ {valor:.2f}\n'
        saldo = valor
    else:
        valor = 0
        saldo = 0
        extrato = ''
        print('Valor inserido é inválido. Refaça a operação!')
    return (saldo, extrato)


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        valor = float(input('Informe o valor de saque. '))
        if valor < 0:
            valor = 0
            saldo = 0
            extrato = ''
            print('Valor inserido é inválido. Refaça a operação!')
        elif valor > limite:
            valor = 0
            saldo = 0
            extrato = ''
            print('Valor superior ao seu limite diário.')
        elif valor > saldo:
            valor = 0
            saldo = 0
            extrato = ''
            print('Saldo insuficiente.')
        else:
            extrato = f'Saque: R$ {valor*-1:.2f}\n'
            saldo = valor
            numero_saques += 1
    else:
        print('Quantidade de saques diários excedido.')
    return (saldo, extrato)


def extrato(extrato, /, *, saldo):
    print('\n>>>>>> EXTRATO BANCÁRIO <<<<<<')
    print('Não existem movimentações a serem mostradas.' if not extrato else extrato)
    print(f'Saldo R$ {saldo:.2f}')
    print('\n>>>>>>> fim do Extrado <<<<<<<')


# Declarando as Variáveis
menu = '''
>>> Digite a Opção Desejada <<<
(u) Cadastro Usuario
(c) Cadastra Conta
(d) Depósito
(s) Saque
(e) Extrato
(q) Sair
'''

# Sistema
while True:
    opcao = input(menu)
    # Cadastro de Usuários
    if opcao == 'u':
        user = (cria_usuario(nome=input('Informe o Nome: '), data_nascimento=input('Informe a Data de Nascimento no formato dd/mm/aaa: '),
                cpf=input('Informe somente os números do CPF: '), endereco=input('Informe o Endereço: ')))
        for us in USUARIOS:
            if user[2] in us:
                print("Usuário já cadastrato!!")
                break
        else:
            USUARIOS.append(user)
    # Cadastro de Contas
    elif opcao == 'c':
        conta = cria_conta(agencia='0001', numero_conta=NR_CONTA, usuario=input(
            'Informeo somente os números do CPF do Correntista: '))
        for us in USUARIOS:
            if conta[2] in us:
                CONTAS.append(conta)
                NR_CONTA += 1
                print(CONTAS)
            else:
                print(
                    'CPF não cadastrado como Correntista, por favor realize o cadastro primeiramente.')
                break
    # Operação de Depósito
    elif opcao == 'd':
        dep = deposito(SALDO, float(
            input('Informe o valor para Depósito. ')), EXTRATO)
        SALDO += dep[0]
        EXTRATO += dep[1]
    # Operação de Saque
    elif opcao == 's':
        saq = saque(saldo=SALDO, valor=0, extrato=EXTRATO, limite=LIMITE_VALOR,
                    numero_saques=QT_SAQUES, limite_saques=LIMITE_SAQUE)
        SALDO -= saq[0]
        EXTRATO += saq[1]
    # Operação de Extrato
    elif opcao == 'e':
        extrato(EXTRATO, saldo=SALDO)
    elif opcao == 'q':
        break
    else:
        print("Opção inválida, encerrando atendimento.")
