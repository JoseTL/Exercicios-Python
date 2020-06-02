
class Pessoa:
    def __init__(self, nome, idade): #contrutor
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    #metodo falar
    def falar(self):
        print(f'{self.nomeclasse} Está falando.... ')

#classe Cliente herdando da pessoa
class Cliente(Pessoa):
    #metodo comprar
    def comprar(self):
        print(f'{self.nomeclasse} está comprando no supermercado! ' )

#classe aluno herdando da Pessoa
class Aluno(Pessoa):
    #metodo estudar
    def estudar(self):
        print(f'{self.nomeclasse} está estudando para a prova da semana que vem ...!')