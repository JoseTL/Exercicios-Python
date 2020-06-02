grupo = list() # definindo ou criando lista
pessoa = dict() # definindo ou criando dicionario
while True: #primeiro while
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')) #defenindo a atribruto nome do tipo string colocando no dicionario
    while True: #segundo while
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]  # upper()[0] siginifica o usário so digita letra maiúscula da primeira letra

        if pessoa['sexo'] in 'MF':  #se o sexo da pessoa é M/F
            break # break da segundo while

        print('ERRO...! Por favor, digite apenas letra M ou F. ') # mostra o erro enquanto digita outra letras
    pessoa['idaded'] = int(input('Idade: '))

    grupo.append(pessoa.copy())
    while True: #terceiro while
        resposta=str(input('Quer continuar? [S/N] ')).upper()[0]

        if resposta in 'SN':
            break #break da terceira while
        print('Erro...! Por favor responda apenas a letra S ou N.')

    if resposta == 'N':
        break # break do primeiro while


print(grupo)