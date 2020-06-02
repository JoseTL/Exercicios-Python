#A confederação nacional de natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo com sua idade: Até 9 anos - MIRIM;
# Até 14 anos - INFANTIL; Até 19 anos - JÚNIOR; 
# Até 20 anos - SENIOR; ACIMA de 20 - MASTER;

from datetime import date
atual = date.today().year
nascimento = int(input("Informe o ano da Nascimento: "))
idade = atual - nascimento
print('O atlata tem {} anos'.format(idade))

if idade<=9:
    print(' Categoria: MIRIN')

elif idade>9 and idade<=14:
    print('Categoria: INFANTIL')

elif idade>14 and idade<=19:
    print(' Categoria: JÚNIOR')

elif idade<=20:
    print('Categoria: SENIOR')

else:
    print('Categoria: MASTER')

    
