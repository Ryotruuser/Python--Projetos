from tkinter import *
from functools import partial

def bt_click(botao):
    print(botao['text'])


janela = Tk()

bt1 = Button(janela, width=20, text='Botão 1')
bt1['command'] = partial(bt_click, bt1)
#O comando partial faz a chamada da função nesse caso.
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text='Botão 2')
bt2['command'] = partial(bt_click, bt2)
bt2.place(x=100,y=130)









janela.geometry('300x300+200+200')
janela.mainloop()