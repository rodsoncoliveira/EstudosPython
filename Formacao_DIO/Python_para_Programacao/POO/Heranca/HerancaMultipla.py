class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def dormindo (self):
        print("Está dormindo, faça silêncio!")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
    
class Mamifero(Animal):
    def __init__(self, cor, **kw):
        super().__init__(**kw)
        self.cor = cor
    
    def leite (self):
        print('Mamifero bebe leite.')

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico
        
    def voando (self):
        print('Está voando!')

class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def comida (self):
        print('O que será que come?')


C = Cachorro(num_patas=4, cor='preto')
print(C)

o = Ornitorrinco(num_patas=4, cor='Preto e Branco', cor_bico='amarelo')
print(o)
o.comida()
o.voando()
o.dormindo()
o.leite()