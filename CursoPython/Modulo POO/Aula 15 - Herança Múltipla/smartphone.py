from eletronico import Eletronico
from log import LogMixin


class SmartPhone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} nao esta ligado.'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} ja esta conectado.'
            print(f'{self._nome} ja esta conectado.')
            self.log_error(error)
            return

        info = f'{self._nome} esta conectado.'
        print(info)
        self.log_info(info)
        self._conectado = True



    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} nao esta conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desconectado'
        self.log_info(info)
        print(info)
        self._conectado = False