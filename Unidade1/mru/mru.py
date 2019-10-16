#UFCG
#Programação 1 - 2019.2
#Juan Salvador da Silva -119210821
#MRU

posicao_inicial = float(input()) #essa linha é para receber a posição que o usuário determinar
velocidade = float(input()) #essa linha é para receber a velocidade que o usuário determiar
tempo = float(input()) #essa linha é para receber o tempo que o usuário determinar

posicao_final = posicao_inicial + (velocidade*tempo) #essa linha é resposável pelo cálculo da posição final

print ("Posição final do móvel") #essa linha representa a saída que o usuário espera
print ("S(%.1f) = %.1f m" % (tempo, posicao_final)) #essa linha representa a saída que o usuário espera

