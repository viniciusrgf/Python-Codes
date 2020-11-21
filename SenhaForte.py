print("Digite as senhas separadas por vírgulas: ")
senhas = input().split(",")
chave = ("a senha é forte: ")
 
for senha in senhas:
    saida1=False
    saida2=False
    saida3=False
    saida4=False
    saida5=False
    saida6=False
    
    if len(senha)>=6 and saida5==False:
        req5=True
    if len(senha)<=12 and saida6==False:
        saida6=True
        for char in senha:
        if (char.isalpha()==True and char.islower()==True and saida1==False):
            saida1=True
        if (char.isdigit()==True and req2==False):
            req2=True
        if (char.isalpha()==True and char.isupper()==True and req3==False):
            req3=True
        if ((char=="$" or char=="#" or char=="@") and req4==False)):
            req4=True
    
    if (req1==True and req2==True and req3==True and req4==True and req5==True and req6==True:)
        if (senha.index(senha)==len(senhas)-1):
            senhas=senha + senhas
        else:
            senhas = senhas + senha +","
print(senhas)'