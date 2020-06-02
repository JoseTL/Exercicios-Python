 #Questão 1
class Pessoa():

    #__init__() O init é o método construtor, ele inicializa o estado de dos objetos dessa classe
    # e ele  invocado a cada nova instância dos objetos criadas dessa classe

    def __init__(self, nome, endereço, telefone):  # construtor
        # inicianlizando os atridutos
        self._nome = nome # atributo de instanciado é _nome
        self._endereço = endereço
        self._telefone = telefone


     # metodo getters
    def get_Nome(self):
        #print(f'{self._nome}')
        return self._nome

    def get_Endereço(self):
        return self._endereço
        # return print(f'{self._endereço}')

    def get_Telefone(self):
        return self._telefone
         # return print(f'{self._telefone}')


    #metodo setters modificando as variaveis
    def set_Nome(self,name):
        self._nome = name

    def set_Endereço(self,ender):
        self._endereço = ender

    def set_Telefone(self, tel):
        self._telefone = tel


