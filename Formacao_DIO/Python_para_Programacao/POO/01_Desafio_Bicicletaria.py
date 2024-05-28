# Criando a classe
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor    = cor
        self.modelo = modelo
        self.ano    = ano
        self.valor  = valor

    # definindo métodos ou ações da classe
    def buzinar(self):
        print("PRINNN PRINNNN PRINNN")
    
    def parar(self):
        print("Parando a Bicicleta!!")

    def correr(self):
        print("Bicicleta correndo......")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha","caloy", 2024, 300)

b1.buzinar()
b1.correr()
b1.parar()

print(b1)