#Automacao para uma importadora de compra e venda de commodities:
#- Soja, Milho, Trigo, Petróleo, etc.

#Precisamos pegar na internet, de forma automática, a cotação de todas as commodites e ver se ela está abaixo do nosso preço ideal de compra. Se tiver, precisamos marcar como uma ação de compra para a equipe de operações.

#Base de Dados: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=share_link




#selenium + wedriver(chromedriver)

#Passo 1:Abir navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get("https://www.google.com")    


#Passo 2: Importar base de dados
import pandas as pd

tabela = pd.read_excel("commodities.xlsx")
print(tabela)

#Passo 3: Para cada produto da base de dados
for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace("ç", "c").replace("é", "e").replace("ú", "u")

    link = f"https://www.melhorcambio.com/{produto}-hoje"
    navegador.get(link)
    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value') #Passo 4: pesquisar o preco do produto
    preco = preco.replace(".", "").replace(",", ".")
    #print(preco)

    tabela.loc[linha, "Preço Atual"] = preco #Passo 5: Atualizar o preco na base de dados



tabela["Preço Atual"] = pd.to_numeric(tabela["Preço Atual"], errors="coerce")
tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]    #Passo 6: Decidir quais produtos comprar
print(tabela)


#exportar para o excel
tabela.to_excel("commodities_atualizado.xlxs", index=False)