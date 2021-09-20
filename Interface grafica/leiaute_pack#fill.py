from tkinter import *

janela = Tk()


lb1 = Label(janela, text='horizontal', bg='white')
lb1.pack(side=TOP, fill=X)


janela.geometry('500x200+600+200')
janela.mainloop()