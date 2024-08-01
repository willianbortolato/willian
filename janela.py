#criandp a primeira janela
from tkinter import *
#cor1='#47d147' #Verde clara
#cor2='#3385ff' #Azul clara
janela = Tk() #T maiusculo py>3
janela.title('Olá mundo') #criando o titulo da janela
janela.geometry('600x250') #deinindo o tamanho da janela 1-largura por x 2-altura
janela.config(bg='#4d0000') #alterar a cor do fundo da janela-recebe background -
#ver colorpicker em htt://www.w3school.com/colors/colors/colors_picker.asp
janela.iconphoto(False, PhotoImage(file='logo1.png'))#alterando o icone da janela
janela.resizable(width=True, height=True)#tornando
janela.mainloop()#sempre no fim do código