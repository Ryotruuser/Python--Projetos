from tkinter import *

janela = Tk()

lb = Label(janela, text='Fala Galera!!')
lb.place(x=100, y=100)

janela.geometry('300x300+200+200')

janela.mainloop()