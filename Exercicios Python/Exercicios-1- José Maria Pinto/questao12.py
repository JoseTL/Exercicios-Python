
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
# seu aumento. Para salários superiores a R$1500, dê um aumento de 10%. Para salários
# menores ou iguais a R$1500 dê um aumento de 15%;
salarios = float(input(" Qual o salário do funcionário:  "))

if salarios <= 1500:
    novosalario = salarios + (salarios * 15/100)
    print('Você deve receber de R${:.2f} '.format(novosalario))
else:
    novosalario = salarios + (salarios*10/100)
    print('Você deve receber de R${:.2f} '.format(novosalario))


