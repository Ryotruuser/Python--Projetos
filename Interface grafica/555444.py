import tkinter as tk


janela = tk.Tk()  # referencia da  janela principal
janela.title('Janela Principal')  # Titulo da janela principal
janela["bg"] = "green"   #alterar cor de fundo da janela
janela.geometry('300x300+450+350') # altera a dimensão da janela e a posição


janela.mainloop()  # loop infinito da janela principal
