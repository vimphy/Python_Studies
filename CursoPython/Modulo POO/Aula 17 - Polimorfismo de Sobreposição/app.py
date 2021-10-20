"""
Polimorfismo é o principio que permite que classes derivadas de um mesma superclasse
tenham métodos iguais (de mesma assinatura) mas comportamentos diferente.

Mesma assinatura = Mesma quantidade e tipos de parâmetros
"""
from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}.')

class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}.')


b = B()
c = C()

b.falar('Oi oi')
c.falar('Alo alo')