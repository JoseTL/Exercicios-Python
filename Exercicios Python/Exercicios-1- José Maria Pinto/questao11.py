# Faça um programa que leia três números e mostre qual é o
#  maior e qual é o menor;

Num1 = int(input('Informe o Primeiro número: '))
Num2 = int(input('Informe o Segundo número : '))
Num3 = int(input('Informe o Terceiro número: '))

# Verificando  qual o valor é maior

if Num1 > Num2 and Num1 > Num3:
    maior = Num1

if Num2 > Num1 and Num2 > Num3:
    maior = Num2

if Num3 > Num1 and Num3 > Num2:
    maior = Num3

print('Maior numero é: {} '.format(maior))

# Verificando  qual o valor é menor

if Num1 < Num2 and Num1 < Num3:
    menor = Num1

if Num2 < Num1 and Num2 < Num3:
    menor = Num2

if Num3 < Num2 and Num3 < Num2:
    menor = Num3

print('Menor número é {} '.format(menor))



