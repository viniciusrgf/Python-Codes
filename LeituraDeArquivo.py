ref = open("acidentes2017.csv", 'r', encoding = 'utf8')
lista = []
c = 0

for linha in ref:
    c += 1
    bairro = linha.split(";")[4].replace('"', '')
    if bairro != '':
    	lista.append(linha)   

print('O arquivo antigo tem:',c, 'linhas.')


limpo = open("acidentes2017_limpo.csv", 'w', encoding = 'utf8')
c = 0

for i in lista:
    c += 1
    limpo.write(i)

print('O arquivo novo tem:',c, 'linhas.')