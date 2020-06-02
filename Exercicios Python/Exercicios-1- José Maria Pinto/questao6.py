#Faça um programa que leia um número de 0 a 9999
# e mostre na tela: qual é o número
# da unidade, dezena, centena e milhar;

numero =int(input("Iforme um número: "))
#numero // 1 significa divisão inteira de 1
uni= numero//1 %10 # ele pega o resto do modulo 10 seria valor unidade
deze= numero//10%10 # ele pega o resto do modulo 100 que seria dezenha
cent=numero//100%10 #
mil= numero//1000% 10
print('Analizando o número {} '.format(numero))
print('Unidade: {} '.format(uni))
print('Dezena: {} '.format(deze))
print('Centena: {} '.format(cent))
print('Milhar: {} '.format(mil))

