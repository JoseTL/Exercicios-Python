#Crie um programa que leia o ano de nascimento de 7 pessoas
# e diga quantas delas já são de maiores;

from datetime import date
atual = date.today().year
totalMaior=0
totalMenor=0
for pessoa in range(1,8):
    nascimento = int(input('Informe o ano do nascimento da {}ª pessoa: '.format(pessoa)))
    idade = atual - nascimento
    if idade >= 21:
        totalMaior += 1

    else:
        totalMenor += 1

print(' {} pessoas com maior idade '.format(totalMaior))
print(' {} pessoas com menor idade '. format((totalMenor)))

