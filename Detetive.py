print("Telefonou para a vítima?")
a = input()
print("Esteve no local do crime?")
b = input()
print("Mora perto da vítima?")
c = input()
print("Devia para a vítima?")
d = input()
print("Já trabalhou com a vítima?")
e = input()
cont = 0
if(a == 'sim'):
    cont = cont + 1
if(b == 'sim'):
    cont = cont + 1
if(c == 'sim'):
    cont = cont + 1
if(d == 'sim'):
    cont = cont + 1
if(e == 'sim'):
    cont = cont + 1

if(cont == 2):
    print("voce é suspeito")
if(cont == 3 or 4):
    print("voce é cumplice")
if(cont == 5):
    print("voce é o assassino")