from abc import ABC, abstractmethod


class desconto_abstrato(ABC):

    def __init__(self, desconto = 0, proximo_desconto=None):
        self.__proximo = proximo_desconto
        self.__desconto = desconto

    @abstractmethod
    def atender_requisicao(self):
        pass

    @property
    def proximo(self):
        return self.__proximo

    @property
    def desconto(self):
        return self.__desconto

class desconto_cupom(desconto_abstrato):

    def atender_requisicao(self, valor):
        if self.desconto != 0:
            return self.desconto * valor
        elif self.proximo is not None:
            self.proximo.atender_requisicao(valor)


class desconto_black_friday(desconto_abstrato):

    def atender_requisicao(self, valor):
        if self.desconto != 0:
            return self.desconto * valor
        elif self.proximo is not None:
            self.proximo.atender_requisicao(valor)


class desconto_quantidade(desconto_abstrato):

    def atender_requisicao(self, valor):
        if self.desconto != 0:
            return self.desconto * valor
        elif self.proximo is not None:
            self.proximo.atender_requisicao(valor)


desc = desconto_black_friday(0.1, desconto_cupom(0.13))
