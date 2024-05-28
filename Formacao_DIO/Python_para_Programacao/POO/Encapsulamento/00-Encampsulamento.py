class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

conta = Conta(100)
conta.depositar(50)
conta.sacar(25)
print(conta._saldo)