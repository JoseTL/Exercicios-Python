#  Elabore um programa que, ao inserir o valor de um produto e sua condição de
# pagamento, ele informe o seguinte: Se for pagamento à vista, mostre o preço do
# produto com 10% de desconto; Se for cartão à vista, mostre o preço com 5% de
# desconto; Se for cartão mas parcelado, mostre o preço do produto 15% mais caro;

print('{:=^60}'.format(' Lojas Online '))
preço = float(input('Informe os preços das compras (R$):  '))
print('''FORMAS DE PAGAMENTO
[1] à vista  
[2] cartão à vista 
[3] cartão parcelado ''')

opção = int(input('Informe o tipo do pagamento: '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('A sua compra de R${:.2f},  vai custar R${:.2f} no final.'.format(preço, total))

elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('A sua compra de R${:.2f},  vai custar R${:.2f} no final.'.format(preço, total))

elif opção ==3:
    total = preço + (preço * 15/100)
    print('A sua compra de R${:.2f},  cartão parcelado vai custar R${:.2f} e 15% mais caro!'.format(preço, total))




