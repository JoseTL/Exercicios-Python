#Crie um programa que leia um número inteiro
#  e mostre na tela se ele é par ou ímpar;
numero=int(input("Informe um número: "))
resultado = numero%2

if resultado==0:
  print('O número que você digitou é {} PAR'.format(numero))

else: 
  print('O número que você digitou é {} IMPAR'.format(numero))
