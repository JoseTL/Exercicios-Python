#Escreva um programa que leia um valor em metros e o exiba convertido em
#centímetros e milímetros; O calculo de conversão deve ser feito em uma função.

def medida(num):
    centimetros = (num * 100)
    milimetros = (num * 1000)
    print(' A medida de {}m corresponde a {}cm e {}mm '.format(metro,centimetros,milimetros))
    
#programa principal
metro = float(input("Informe uma medida: "))
medida(metro)


