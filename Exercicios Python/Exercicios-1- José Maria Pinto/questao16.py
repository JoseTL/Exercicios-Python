#Desenvolva um programa que leia seis números inteiros e
# mostre a soma total apenas daqueles que forem ímpares;

soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(c)))

    if numero % 2 == 1 :
        soma = soma + numero
        cont += 1

print('Você informou {} números IMPARES e a soma dos números foi {} '.format(cont,soma))
