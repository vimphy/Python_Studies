# Setter =  Configurar um valor (=)
# Getter = Obter um valor (.)


class Pessoa:
    def __init__(self, nome):
        self._nome = nome


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return 'DESCONHECIDO'


p1 = Pessoa('Rennan')
print(p1.nome)
print(p1.sobrenome)