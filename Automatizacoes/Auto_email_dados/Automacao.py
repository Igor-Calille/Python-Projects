#Automaçao simples para resposder um email de forma automatica com a obtenção de dados de uma empresa




#automatizar mouse, teclado, tela...
#pip install pyautogui
import pyautogui
import time


pyautogui.PAUSE = 0.2

##Passo 1: Entrar no sitema da empresa
#pyautogui.click #mouse
#pyautogui.write #texto
#pyautogui.press #tecla
#pyautogui.hotkey #apertar uma combinacao de teclas

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
#pyautogui.hotkey("ctrl", "t")
pyautogui.press("enter")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")


##Passo 2: Fazer login
#clicar no espaço de login e escrever
#print(pyautogui.position())

#login
pyautogui.click(x=2829, y=346)
pyautogui.write("Meu Login")
#login
pyautogui.click(x=2799, y=424)
pyautogui.write("senha123")
#acessar
pyautogui.click(x=2873, y=492)


##Passo 3: exportar base de dados


#download
#time.sleep(3)
pyautogui.doubleClick(x=2319, y=357)
#time.sleep(4)
pyautogui.click(x=3750, y=103)


##passo 4: cal indicadores
import pandas
import numpy
import openpyxl
import pyperclip

tabela = pandas.read_csv(r"C:\Users\igorm\Downloads\Compras.csv", sep =";")
print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quant = tabela["Quantidade"].sum()
preco_medio = total_gasto / quant

print(total_gasto)
print(quant)
print(preco_medio)


##Passo 5: enviar email

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
#pyautogui.hotkey("ctrl", "t")
pyautogui.press("enter")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

#escrever email
time.sleep(2)
pyautogui.click(x=2015, y=162)

#destinatario
time.sleep(1)
pyautogui.write("igormassoncalille123@gmail.com")

#assunto
time.sleep(1)
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório")
pyautogui.hotkey("ctrl", "v")

#corpo
time.sleep(1)
pyautogui.press("tab")

texto =f"""
Prezados,

Total gasto: {total_gasto:,.2f}
Quantidade de produtos: {quant}
Preço médio: {preco_medio:,.2f}

ass:Ig Ca

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")



#enviar
pyautogui.hotkey("ctrl", "enter")