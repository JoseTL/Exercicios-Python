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



# Questão 2
#classe fornecedor
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


 #Questão 3
class Empregado(Pessoa):
    def __init__(self,nome, endereço, telefone,codigoSetor, salarioBase,imposto): #construtor
        Pessoa.__init__(self,nome, endereço, telefone) #construtors da classe Pessoa
        #inicializando atrib    passutos desta classe
        self._codigoSetor = codigoSetor
        self._salarioBase = salarioBase
        self._imposto = imposto

    # metodo getters
    def get_CodigoSetor(sel):
        return sel._codigoSetor

    def get_SalarioBase(sel ):

        return sel._salarioBase

    def get_Imposto(self):
        return self._imposto


    # metodo setters
    def set_CodigoSetor(self, codigo):
        self._codigoSetor = codigo

    def set_SalarioBase(self, salario):
        self._salarioBase = salario

    def set_Imposto(self, valor):
        self._imposto = valor

    #metodo calcular salario
    def calculaSaldo(self,_salarioBase):
        if self._salarioBase <= 1900:
            valor = 3/100
            print('Imposto')
        elif self._salarioBase <= 2500 and self._salarioBase <= 4000:
            valor = 7/100

        elif self._salarioBase <= 4500 and self._salarioBase <=10000:
            valor=12/100;
        else:
            valor =15/100
        return self._salarioBase - valor/100



p1 = Pessoa("Kaio Nunes", "Rua Belo, 23", "123-3456-7665")
f=Fornecedor("Kaio Nunes", "Rua Belo, 23", "123-3456-7665", 9000.45, 323.00)
em=Empregado("Maria da Silva"," Rio Rande,11", "323-3654-7877", 123, 5000, 400.99)
print('Fornecedor: ', f.get_Nome(),'tem valor credito de: ', f.set_ValorCredito(400.32), 'e ele tem a divida de ',f.get_ValorDivida())
print('Empregado/a: ', em.get_Nome(),'tem salario de ', em.get_SalarioBase(), 'e tem o seu imposto de ', em.set_Imposto(10.0))