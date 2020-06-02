
#Desenvolva um programa que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com 
# as informações: < 18.5 - Abaixo do peso; entre 18.5 e 25 - Peso ideal; 
# 25 até 30 - Sobrepeso; 30 até 40 - Obesidade; 
# Acima de 40 - Obesidade Mórbida;

peso = float(input("Informe o peso da pessoa (KG): "))
altura = float(input("Informe a sua altura (m) "))
imc = peso/(altura**2)
print('o Seu IMC é: {:.1f}'.format(imc))

if imc<18.5:
    print(' - Abaixo do peso')

elif 18.5 <= imc < 25:
    print(' - Peso Ideal')

elif 25 <= imc < 30:
    print(' - Sobrepeso')

elif 30 <= imc < 40:
    print(' - Obesidade')

else:
    print(' - Obesidade Mórbida')