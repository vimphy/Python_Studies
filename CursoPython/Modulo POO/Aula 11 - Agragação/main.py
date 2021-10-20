"""
Na Agregação as classes podem existir sozinhas mas dependem umas das outrar para
que suas caracteristicas façam sentido completo.

Ex:. Um carro e suas rodas existem normalmente sem depender um do outro,
porém o carro precisa das rodas para que possa
ser dirigido normalmente e cumprir sua função.
"""

from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Mochila', 70)
p3 = Produto('Tenis', 45)
p4 = Produto('Bone', 25)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)
carrinho.inserir_produto(p1)
carrinho.listar_produto()

print(f'O valor total da compra é: R${carrinho.soma_total()},00')