CONTAS = []
USUARIOS = [['rodson','30/11/1981','123','rua 15']]
NR_CONTA = 1
cont = [1,2,3]

def cria_conta(agencia,numero_conta, usuario):
    conta = [agencia, numero_conta, usuario]
    return conta

for i in cont:
    conta = cria_conta(agencia='0001',numero_conta=NR_CONTA,usuario=input('Informeo somente os números do CPF do Correntista: '))
    for us in USUARIOS:
        if conta[2] in us:
            CONTAS.append(conta)
            NR_CONTA += 1
            print(CONTAS)
        else:
            print('CPF não cadastrado como Correntista, por favor realize o cadastro primeiramente.')
            break