from abc import ABC, abstractmethod


class ImpostosAbstrato(ABC):

    @abstractmethod
    def calcula(self):
        pass


class ICMS(ImpostosAbstrato):

    def calcula(self, valor):
        return valor * 0.11


class ISS(ImpostosAbstrato):

    def calcula(self, valor):
        return valor * 0.05


class PIS(ImpostosAbstrato):

    def calcula(self, valor):
        return valor * 0.025
