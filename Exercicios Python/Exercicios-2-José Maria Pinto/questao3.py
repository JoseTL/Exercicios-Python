#Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
#   a. Quantas pessoas foram cadastradas;
#   b. A média de idade do grupo;
#   c. Uma lista com todas as mulheres;
#   d. Uma lista com todas as pessoas com idade acima da média;

grupo = list() #defenido lista grupo
pessoa = dict() # definindo dicionario
soma = media = 0

while True: # 1º while

    pessoa.clear() # esvaziar pessoa
    pessoa['nome'] = str(input('Nome: ')) #defenindo a atribruto nome do tipo string colocando no dicionario

    while True: # 2º while
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]  # upper()[0] siginifica o usário so digita letra maiúscula da primeira letra

        if pessoa['sexo'] in 'MF': #se o sexo da pessoa é M/F
            break # 2º while
        print('ERRO...! Por favor, digite apenas M ou F') # mostra o erro enquanto digita outra letras

    pessoa['idade'] = int(input('Idade: ')) # defenindo atributo idade do tipo inteiro e colocando no dicionario

    soma += pessoa['idade']

    grupo.append(pessoa.copy()) #lista pessoa vai receber uma coopis

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resp in 'SN':
            break # 3º while
        print('ERRO...! Responda apenas S ou N ')

    if resp == 'N':
        break # 4º while

print('='*80) #para fazer separador  da lista

#imprimindo pessoas cadastradas
print(f' A) Foram {len(grupo)} pessoas cadastradas.') # len(grupo) para mostrar tamanho da lista do grupo

media = soma / len(grupo) # calculando da idade media da pessoa cadastrado
# imprimir a idade media da pessoa cadastrado no grupo
print(f' B) A média da idade do grupo é  {media:5.2f} anos.')


# imprimir mulheres cadastrados
print(' C) As melheres cadastradas foram ', end=' ')
for pESSOA in grupo:
    if pESSOA['sexo'] in 'Ff':
        print(f'{pESSOA["nome"]}, ', end=' ')
print()

print(' D) As Pessoas estão na lista acima da média são: ')
for pESSOA in grupo:
    if pESSOA['idade'] >= media:
        print('     ', end=' ')
        for chave,valor in pESSOA.items():
            print(f'{chave}={valor},', end=' ')
        print()

print('<<<<<<<< O PROGRAMA ENCERRADO!  >>>>>>')









