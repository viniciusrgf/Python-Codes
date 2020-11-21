cima = 1
baixo = 1
esquerda = 1
direita = 1
while(cima  != 0 or esquerda != 0 or baixo != 0 or direita != 0):
    print("digite qnts passos o robo vai pra cimna")
    cima = int(input())
    print("digite qnts passoa pra baixo")
    baixo = int(input())
    print("digite qnts passos ele vai pra esquerda")
    esquerda = int(input())
    print("qnts para direita")
    direita = int(input())
    if(cima>=baixo):
        vertical = cima - baixo
    else:
        vertical = baixo - cima
    if esquerda >= direita:
        horizontal = esquerda - direita
    else:
        horizontal = direita - esquerda
    distancia = ((horizontal**2)+(vertical**2))**1/2
print(distancia)