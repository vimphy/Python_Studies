"""
Composição é a relação mais forte entre classes.

Nela uma classe é "Dona" de objetos de outra classe.

Se a classe principal for apagada todos os objetos que a classe utilizou serão
apagados com ela
"""

from classes import Cliente, Endereco


cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listar_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.listar_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.listar_enderecos()
del cliente3
print()

print('#################################################################')