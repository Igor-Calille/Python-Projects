import tkinter as tk
from tkinter import * 
from tkinter import ttk
import ScrapingPecas_MercadoLivre as ML
import time
import asyncio
import threading

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

async def wait():
    await asyncio.sleep(0.4)


# Configuração da janela
janela = tk.Tk()
img_MH = PhotoImage(file="Logos\MH.png")
janela.iconphoto(False, img_MH)
janela.title("Consulta de Web Scraping")
janela.geometry("600x250")
janela.configure(bg='black')
frame_vermelho = Frame(janela, bd=4, bg='red', highlightbackground='grey', highlightthickness=3)
frame_vermelho.place(relx=0.1, rely= 0.1, relwidth=0.80, relheight=0.7)



#Adicionando imagem MotorHero
img_MotorHero = PhotoImage(file="Logos\MotorHero.png")
img_MotorHero = img_MotorHero.subsample(3,3)
label_imagem_MotorHero = Label(janela, image=img_MotorHero, highlightbackground='grey', highlightthickness=3)
label_imagem_MotorHero.pack(pady=10)

# Rótulo de instrução
label = tk.Label(janela, text = "Forneça o link do mercado livre que deseja fazer a pesquisa:", fg="black", bg="red")
label.pack(pady=10)

# Entrada de texto
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

def ProgressBar(pb1):
    

    for i in range(10000):
        janela.update_idletasks()
        pb1['value'] += 20

        asyncio.run(wait())

def Scraping():
    ML.processoInicial(entrada.get())
    #pb1.stop()

    pb1 = tk.Label(janela, text = "Processo finalizado!")
    pb1.pack(pady=10)

def script():
    #pb1 = ttk.Progressbar(janela, orient=HORIZONTAL, length=200, mode='indeterminate')
    #pb1.pack(pady=20)
    t1 = threading.Thread(target=Scraping())
    #t2 = threading.Thread(target=ProgressBar(pb1))
    

    t1.start()
    #t2.start()
    
    t1.join()
    #t2.join()
    


# Botão de pesquisa
botao_pesquisar = tk.Button(janela, text="Pesquisar", command=lambda: script(), bg="red", fg="black")
botao_pesquisar.pack()


# Loop principal
janela.mainloop()