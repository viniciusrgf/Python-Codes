entrada=input("Digite: ").split(" ")
alfabeto="[a-z]"
if len(entrada) == 1:
    p=False
else:
    for elemento in entrada:
              if entrada.index(elemento)==(len(entrada)-1):
            frase+=elemento
            
 
    if len(entrada[0])<4:
        print("Erro.")
        passagem=False
 
        else:
            print("Erro.")
            passagem=False
 
if p==True:
    rot=int(entrada[0][3:])
 
    if rot==26 or rot==0:
        print(frase)
    else:
        for letra in frase:
            if letra==" ":
                saida+=letra
            else:
                if rot > 26-(alfabeto.index(letra.lower())+1):
                    if letra.isupper()==True:
                        saida += alfabeto[rot-(26-((letra.lower())))].upper()
                    else:
                        saida += alfabeto[rot-(26-((letra.lower())))]
                else:
                    if letra.isupper()==True:
                        saida += alfabeto[rot + (letra.lower())].upper()
                    else:
                        saida += alfabeto[rot + letra.lower())]
    print(saida)