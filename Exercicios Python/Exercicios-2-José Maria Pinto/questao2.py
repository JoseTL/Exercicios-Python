#Crie um programa que leia vários números e os coloque em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares da primeira lista, respectivamente. No final,
# mostre o conteúdo das três listas geradas.

num = list() #definindo a lista geral
ímpares = list() #defenindo lista impares
pares = list() #defenindo lista pares
while True:
    num.append(int(input('Digite um número: '))) #informe ao usuário digitar um valor
    #resposta = str(input('Quer continuar? [S/N] ')) # digita S para continuar e N para terminar
    if resposta in 'Nn':  # configura o usário digitar a letra N maiuscula e tanto minúscula no teclado
        break
    print('ERRO...! Por favor, digite apenas S ou N')  # mostra o erro enquanto digita outra letras

for i,valor in enumerate(num): # setando o valor na lista geral
    if valor % 2 == 0: #se o numero digita divide por 2 e seu resto 0
        pares.append(valor) #então numero é par e armagenando no valor na lista
    elif valor % 2 == 1:  #se o numero digita divide por 2 e seu resto 1
        ímpares.append(valor)  #então numero é impar e armagenando no valor na lista

print('='*90)
#imprimindo os valores na lista
print(f'A lista completa é {num} ')
print(f'A list de pares é {pares} ')
print(f'A lista de Ímpares é {ímpares}')



