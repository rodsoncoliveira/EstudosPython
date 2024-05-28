class Veiculo:
    def __init__(self, cor, placa, num_rodas):
        self.cor        = cor
        self.placa      = placa
        self.num_rodas  = num_rodas

    def ligar_motor (self):
        print("Motor Ligado!")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} estou carregado')

v1 = Motocicleta('branca', '123', 2)
v1.ligar_motor()

caminhao = Caminhao('preto', 'abc-1234', 16, False)
caminhao.esta_carregado()
print(caminhao)