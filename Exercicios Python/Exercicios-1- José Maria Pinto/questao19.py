#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final, mostre: A média de idade do grupo;
#Qual o nome do homem mais velho; Quantas mulheres têm menos de 20 anos;

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totalMulher20 = 0
for pessoa in range(1,5):
    print(' ---- {}ª  Pessaos ----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '));
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm':
      maioridadehomem = idade
      nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 +=1


médiaidade=somaidade/4
print('A média de idade do grupo é de: {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('{} mulheres com menos de 20 anos'.format(totalMulher20))





