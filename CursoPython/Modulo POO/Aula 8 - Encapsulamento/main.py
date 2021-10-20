"""
# Encapsulamento serve para esconder partes do código.

Forma clássica da maioria das linguagens:
    modificadores:
        public (métodos que podem ser acessados dentro e fora da classe),
        protected (métodos e atributos que só podem ser acessados dentro da classe
        ou em suas classes filhas),
        private (Tal atributo ou método só está disponível na classe)

Convenções para python
_   Atributos ou métodos com 1 underline recomenda-se
    que não seja acessado (Protected ou Private Fraco).

__  Atributos ou métodos  com 2 underlines recomenda-se
    fortemente que não seja modificado (Private Forte)

"""

class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados


    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Jorge')
bd.inserir_cliente(2, 'Liz')
bd.inserir_cliente(3, 'Ronaldo')
bd.inserir_cliente(4, 'Itinho')
# bd.dados = 'Outro valor'
print(bd.dados)