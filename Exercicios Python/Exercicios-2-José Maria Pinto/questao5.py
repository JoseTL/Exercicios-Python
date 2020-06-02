#Crie um programa que gerencia o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois, o programa deve ler quantos gols o jogador fez em cada partida,
# calcular o total de gols e guardar tudo isso em um mesmo dicionário.

jogador = dict() #declarando lista de jogador com parametro vazio
partidas = list() # declarando lista de partidas com parametro vazio
jogador['nome'] = str(input('Nome do Jogador: ')) # declarando variavel em um aray
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? ')) #declarando variavel  de total golo pasando parametro nome
for c in range(0,tot):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}? '))) # c+1 signifca ele vai imprimir começha no indexe 1
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas) # somar os golos nas partidas

print('='*80) # para fazer seperação igual
print(jogador)
print('='*80) # para fazer seperação igual

for k, valor in jogador.items():
    print(f'O campo {k} tem o valor {valor}')

print('', '='*80) # para fazer seperação igual
#imprimindo
print(f' O jogador {jogador["nome"]}, jogou {len(jogador["gols"])} partidas.') # len é para configuração a impreção com legivel

for i, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1} fez {valor} gols. ')  # c+1 signifca ele vai imprimir começha no index
print(f'E fez o total de {jogador["total"]} gols nas partidas que  jogou.')
print('='*80, '\n') # para fazer seperação igual