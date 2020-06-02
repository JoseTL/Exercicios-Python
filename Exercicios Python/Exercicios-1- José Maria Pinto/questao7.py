#Crie um programa que leia o nome
# de uma pessoa e diga se ela tem Silva no nome;

nome =str(input('Informe o seu nome completo: ')).strip()
 # "silva in nome" significa setar o silva dentro de nome
print('O seu nome tem Silva? {} '.format('silva' in nome.lower())) # "nome.lower()" significa ENTRE com minúscula de nome silva
#print('O seu nome tem Silva? {} '.format('SILVA' in nome.upper()))# "nome.upper()" significa ENTRE com Maiúscula de nome SILVA
