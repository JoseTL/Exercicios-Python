#Faça um programa que leia a largura e altura de uma parede em metros e calcule a sua
#área. Em seguida, mostre também a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m2;

largura =float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
área = largura * altura
print("A parede tem a dimenção de {}x{} metros e sua Área é de {}m². ".format(largura,altura,área))
tinta = área / 2
print('Para pintar essa parede, você precisa de {}l de tinta.'.format(tinta))
