#Crie um programa capaz de ler vários números e colocá-los em uma lista. Depois disso, mostre:
#   a. Quantos números foram digitados;
#   b. A lista de valores ordenada de forma decrescente;
#   c. Se o valor 5 está ou não dentro da lista;

valores =[ ]
while True:
    valores.append(int(input( ' Digite um valor: ')))
    resp = str(input(' Quer continuar: [S/N] '))
    if resp in 'Nn':
        break

print('='*90)
print(f'Vocẽ digitou {len(valores)} elementos.')
valores.sort(reverse= True) # ele vai inverter os números em ordem decrescente
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')