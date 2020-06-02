#Faça um algoritmo que leia o preço de um produto e o desconto e mostre seu novo
# preço com de desconto; O calculo do desconto deve ser feito em uma função.

def produto(preço, desconto):
    novopreço = preço-(preço*desconto/100)
    print('O preço  do produto com o desconto é R$ {:.2f}'.format(novopreço))

#programa principal
p=float(input("Informe o preço do produto (R$): "))
d=float(input("Informe o desconto: "))
produto(p,d)


