from classes import *
"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É

Herança
\
 \
  \
   \
    \
     \
      \
       \
        Herdeiro
"""

c1 = Cliente('Rennan', 34)
c1.falar()
c1.comprar()

a1 = Aluno('Paulo', 19)
a1.falar()
a1.estudar()

p1 = Pessoa('João', 43)
p1.falar()