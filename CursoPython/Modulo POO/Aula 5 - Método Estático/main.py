from random import randint
class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod            # Método de Classe
    def por_ano_nasc(cls, nome, ano_nascimento):   # Sempre utilizar a abreviação cls
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod          # Método Estático
    def gera_id():
        rand = randint(10000, 19999)
        return rand


#p1 = Pessoa.por_ano_nasc('Rennan', 1996)
p1 = Pessoa('Rennan', 23)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print(p1.gera_id())