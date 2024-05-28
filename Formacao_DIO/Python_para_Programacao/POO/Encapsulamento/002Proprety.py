class Pessoa:
    def __init__(self, nome, ano_nasc) -> None:
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nasc

pessoa = Pessoa('Rodson',1981)
print(f'A pessoa: {pessoa.nome} tem \t{pessoa.idade} anos de idade')