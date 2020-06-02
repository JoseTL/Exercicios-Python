#Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$0.50 por Km
# para viagens até 200Km e R$0.45 para viagens mais longas;

distancia = float(input("Qual é a distãncia da sua viagem? "))
print('Você está presta a  viagem de {} KM'.format(distancia))

'''
if distancia<=200:
  preço = distancia*0.50
else: preço = distancia *0.45 '''

# outra forma usando IF inline
preço=distancia*0.50 if distancia<=200 else distancia*0.45
print('O preço da sua viagem será de {:.2f} Reais'.format(preço))


