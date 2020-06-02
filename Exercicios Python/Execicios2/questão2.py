#Crie um programa que leia vários números e os coloque em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares da primeira lista, respectivamente. No final,
# mostre o conteúdo das três listas geradas.

pares = list()
ímpares = list()
num = list()
while True:
    num.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break

for i,valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        ímpares.append(valor)

print('='*90)
print(f'A lista completa é {num} ')
print(f'A list de pares é {pares} ')
print(f'A lista de Ímpares é {ímpares}')



