#Escreva um programa que leia a velocidade de um carro. Se ele não ultrapassar
#80Km/h, deseje a ele boa viagem, senão, mostre a ele duas mensagens: uma
#mensagem dizendo que ele foi multado e outra com o valor total da multa (R$50.00
#por cada Km acima do limite);

velocidade = float(input("Qual é a velocidade do veículo:  "))

if velocidade > 80:
    print('MULTADO...! você excedeu o limite permitido que é 80 Km/h')
    multa = (velocidade-80) * 50
    print('Você deve pagar a multa de R${:.2f} '.format(multa))
else:
    print('Boa Viagem...!')


