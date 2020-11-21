opcao = 0
print("digite a sa jogada")
while(opcao ==0):
    jogada1 = int(input())
    jogada2 = int(input())
    jogada = [["0","1","2"],["0","1","2"],["0","1","2"]]
    opcao = input()
    lista = []
    lista.append(jogada1)
if(jogada[0][0] == jogada[1][0] == jogada[0][2] or jogada[0][1] == jogada[1][1] == jogada[2][1] or jogada[0][2] == jogada[1][2] == jogada[2][2]):
    print("jogador ")
    
def jogo():
    for i in range(3):
        soma = jogada[i][0]+jogada[i][1]+jogada[i][2]
        if soma==3 or soma ==-3:
            return 1

     
    for i in range(3):
        soma = jogada[0][i]+jogada[1][i]+jogada[2][i]
        if soma==3 or soma ==-3:
            return 1

    
    diagonal1 = jogada[0][0]+jogada[1][1]+jogada[2][2]
    diagonal2 = jogada[0][2]+jogada[1][1]+jogada[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0
if(jogo() = 1):
print("jogador 1 ganhou")
else:
    print("jogador 2 ganhou")
    
