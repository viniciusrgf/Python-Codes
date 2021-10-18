import requests
from tkinter import *
import random

def aleatorio():
    with open ("memesafazer.txt", "r") as arquivo:
        lista = arquivo.readlines()
        arquivo.close
        texto_aleatorio["text"] = random_num = random.choice(lista)
def alfabetica():
    with open ("memesafazer.txt", "r") as arquivo:
        lista = arquivo.readlines()
        arquivo.close
        texto_alfabetico["text"] = sorted(lista)
def visualizar():
    with open ("memesafazer.txt", "r") as arquivo:
        lista = arquivo.read()
        arquivo.close
        texto_visualizar["text"] = lista
def adicionar():
    with open ("memesafazer.txt", "a") as arquivo:
        novo = adicionar_botao.get()
        arquivo.write(novo)
        arquivo.write('\n')
        arquivo.close
        adicionar_botao.delete(0, END)
def remover():
    op = remover_botao.get()
    lista = open("memesafazer.txt", "r")
    lines = lista.readlines()
    lista.close()
    lista2 = open("memesafazer.txt", "w")
    for line in lines:
        if line.strip("\n") != op:
           lista2.write(line)
    lista2.close()
    lista51 = open("memesfeitos.txt", "a")
    lista51.write(op)
    lista51.write('\n')
    lista51.close
    remover_botao.delete(0, END)

janela = Tk()
janela.title("Database")
texto_orientacao = Label(janela,text = "Menu")
texto_orientacao.grid(column=0,row=0,padx=10,pady=10)
opcao_1 = Button(janela,text = "Adicionar",command=adicionar)
opcao_1.grid(column=0,row=1,padx=10,pady=10)
opcao_2 = Button(janela,text = "Visualizaar",command=visualizar)
opcao_2.grid(column=0,row=2,padx=10,pady=10)
opcao_3 = Button(janela,text = "Remover",command=remover)
opcao_3.grid(column=0,row=3,padx=10,pady=10)
opcao_alfabetica = Button(janela,text = "Ordenar Alfabeticamente",command=alfabetica)
opcao_alfabetica.grid(column=5,row=5,padx=10,pady=10)
opcao_aleatoria = Button(janela,text = "Selecionar Um Aleatoriamente",command=aleatorio)
opcao_aleatoria.grid(column=6,row=5,padx=6,pady=10)
texto_aleatorio = Label(janela,text = "")
texto_aleatorio.grid(column=6,row=6,padx=10,pady=10)
texto_alfabetico = Label(janela,text = "")
texto_alfabetico.grid(column=5,row=6,padx=10,pady=10)
texto_visualizar = Label(janela,text = "")
texto_visualizar.grid(column=0,row=4,padx=10,pady=10)
adicionar_botao = Entry(janela)
adicionar_botao.grid(column=1,row=1,padx=10,pady=10)
remover_botao = Entry(janela)
remover_botao.grid(column=1,row=3,padx=10,pady=10)


janela.mainloop()