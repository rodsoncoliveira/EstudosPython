usuarios = []
cont = [1,2,3]
def cria_usuario(nome,data_nascimento,cpf,endereco):
    usuario = [nome,data_nascimento,cpf,endereco]
    return usuario

for i in cont:
    user = (cria_usuario(nome=input('Informe o Nome: '),data_nascimento=input('Informe a Data de Nascimento no formato dd/mm/aaa: '), cpf=input('Informe somente os números do CPF: '), endereco=input('Informe o Endereço: ')))
    for us in usuarios:
        if user[2] in us:
            print("Usuário já cadastrato!!")
            break
    else:
        usuarios.append(user)


print(usuarios)