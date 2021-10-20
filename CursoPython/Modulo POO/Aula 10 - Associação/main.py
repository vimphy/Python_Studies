"""
Associação - As classes se relacionam entre sí, porém elas não dependem uma da outra
para funcionar.
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaEscrever

# Intanciando objetos individualmente
escritor = Escritor('Rennan')
caneta = Caneta('BIC')
maquina = MaquinaEscrever()

# Relacionando objetos a partir de métodos
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# Deletando instância da classe principal
del escritor

# Demostrando que as outra instancias continuam funcionando independentes.
print(caneta.marca)
maquina.escrever()

