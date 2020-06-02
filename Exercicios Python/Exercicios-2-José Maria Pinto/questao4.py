#Faça um programa que leia o nome e a média de um aluno e guarde-os
# em um dicionário. Em seguida, a partir da média, gera a situação final do
# aluno “AP” ou “RP” e também guarde no dicionário. No final mostre o conteúdo do dicionário.


aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

#a media do aluno vai ser 7
if aluno['media'] >= 7: #se a media maior ou igual 7
    aluno['situação'] = 'AP' # situaçao do aluno aprovado
elif 5 <= aluno['media'] < 7: # se a media do aluno entre o intervalo 5 e 7  então
    aluno['situação'] = 'Recuperação' # situação vai fazer prova recuperaão
else:
    aluno['situação'] = 'RP' # se não a situação é reprovado

print('-='*20) #para fazer separador  com a resposta
for chave, valor in aluno.items(): # a chave e o valor do aluno no item
    print(f' - {chave} é  {valor}') # salva numa dicionario ou lista

