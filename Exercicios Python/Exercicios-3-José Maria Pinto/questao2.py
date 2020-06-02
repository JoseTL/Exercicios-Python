# Questão 2
#classe fornecedor
from questao1 import Pessoa
class Fornecedor(Pessoa):

    def __init__(self,nome, endereço, telefone, valorCredito, valorDivida): #construtor
        Pessoa.__init__(self,nome, endereço, telefone)# construtor da classe Pessoa
        #inicializando atributos desta classe
        self._valorCredito = valorCredito
        self._valorDivida = valorDivida

    # metodo getters
    def get_ValorCredito(self):
        return  self._valorCredito

    def get_ValorDivida(self):

        return self._valorDivida


    #metodo setters  modificando as variaveis
    def set_ValorCredito(self, valorCredito):
        self._valorCredito = valorCredito

    def set_ValorDivida(self,valorDivida):
        self._valorDivida = valorDivida


    #metodo obtersaldo
    def obtersaldo(self, valorCredito):
        if self._valorCredito <= 5000.00:
            empresta = 1000.00

        elif self._valorCredito <= 10000.00:
            empresta = 3000.00

        elif self._valorCredito <= 15000.00:
            empresta = 4000.00

        else:
            empresta = 5000.00

        return self._valorCredito == valorCredito - empresta

