class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print('Dispositivo ja esta ligado.')
            return
        else:
            print('Dispositivo Ligado.')
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            print('Dispositivo ja esta desligado.')
            return
        else:
            print('Dispositivo Desligado.')
            self._ligado = False
