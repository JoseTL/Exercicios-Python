# Crie um programa que leia dois valores e mostre um menu na tela
# com as seguintes opções: 1 – Somar; 2 – Multiplicar;
# 3 – Qual é o maior número; 4 – Sair do programa;

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

opção = 0

while opção !=4:
    print('''  [1] - Somar
  [2] - Multiplicar
  [3] - Qual é o maior número
  [4] - Sair do programa
     ''')

    opção = int(input('>>>>>> Escolha uma Operação: '))

    if opção == 1:
        soma = num1 + num2
        print('A soma entre {}+{}  é: {}'.format(num1, num2, soma))

    elif opção == 2:
        Multiplicar = num1 * num2
        print(' O resultado da multiplucação entre {}x{} é: {}'.format(num1, num2, Multiplicar))

    elif opção == 3:
        if num1 > num2:
            maior = num1

        else:
            maior = num2

        print('Entre {} e {} o maior número é: {}'.format(num1, num2, maior))

    elif opção == 4:
        print('Finalizando...! ')
    else:
        print('Opção que você digitou é inválida. Tenta novamente com Opção!')

print('Fim da execução do Program! ')