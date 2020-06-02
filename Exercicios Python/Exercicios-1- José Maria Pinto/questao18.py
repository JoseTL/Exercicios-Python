#Faça um programa que leia o peso de cinco pessoas e
# no final mostre qual foi o maior e o menor peso lido;

maiorpeso = 0
menorpeso = 0

for peso in range(1, 6):
    pesos = float(input('Peso da {}ª pessoa: '.format(peso)))
    if peso==1:
        maiorpeso=pesos
        menorpeso=pesos
    else:
        if pesos > maiorpeso:
            maiorpeso=pesos
        if pesos < menorpeso:
            menorpeso = pesos
print('O maior peso lido foi de {}Kg '.format(maiorpeso))
print('O menor peso foi lido de {}Kg '.format(menorpeso))
