from bs4 import BeautifulSoup
import requests
import asyncio
import time
from PIL import Image
from io import BytesIO
import os
from pathlib import Path
import urllib.request
import pandas as pd

async def wait():
    await asyncio.sleep(1)
    print("1 sec\n")

def retirarBarra(text_entrada):
    # Caractere a ser substituído e caractere de substituição
    caractere_alvo = "/"
    caractere_substituto = "-"

    # Inicialize uma nova string
    novo_texto = ""

    # Percorra a string e substitua o caractere, se encontrado
    for caractere in text_entrada:
        if caractere == caractere_alvo:
            novo_texto += caractere_substituto
        else:
            novo_texto += caractere

    return novo_texto

#def comparacaoPartNumbers():
#    partNumber_enriquecidos = pd.read_excel('excel_partNumberEnriquecidos/PartNumbers.xlsx')
#    print(partNumber_enriquecidos.head())

def scraping(pecaAtual, nomeArquivo):
    pagePeca = requests.get(pecaAtual)
    soup_1 = BeautifulSoup(pagePeca.text, 'html.parser')
    #soup_1 = soup_1.get_text()

    #asyncio.run(wait())

    nomes = soup_1.find_all(class_ = 'ui-pdp-title')
    nomes_clean = [nome.text for nome in nomes]
    print(nomes_clean)

    null_list = []
    
    precos = soup_1.find_all(class_= 'andes-money-amount__fraction')
    precos_clean = [preco.text for preco in precos]
    preco = precos_clean[0]
    cents = soup_1.find_all( class_ = 'andes-money-amount__cents andes-money-amount__cents--superscript-36')

    cents_clean = [cent.text for cent in cents]

    if cents_clean != null_list:
        preco = preco + ',' + cents_clean[0]


    #sales = soup_1.find_all( class_ = 'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact')
    #sales_clean = [sale.get('content') for sale in sales ]
    #cents_sales = soup_1.find_all( class_ = 'andes-money-amount__cents andes-money-amount__cents--superscript-36')
    #cents_sales_clean = [cent_sale.text for cent_sale in cents_sales]
    
    #sale = ''
    #if  cents_sales_clean != preco_null:
    #   sale = ' -> ' + sales_clean[1] + ',' + cents_sales_clean[1]

    heads = soup_1.find_all(class_ = 'andes-table__header__container')

    #De vez em quando o BeatifulSiup retornava uma lista vazia de heads e infos, dessa forma
    #   tive que criar um loop q caso o prograna receba um valor nulo, ele refaz o pedido e analise do html
    while heads == null_list:
        pagePeca = requests.get(pecaAtual)
        soup_1 = BeautifulSoup(pagePeca.text, 'html.parser')
        heads = soup_1.find_all(class_ = 'andes-table__header__container')

    heads_clean = [head.text for head in heads ]

    infos = soup_1.find_all(class_ = 'andes-table__column--value')

    while infos == null_list:
        pagePeca = requests.get(pecaAtual)
        soup_1 = BeautifulSoup(pagePeca.text, 'html.parser')
        infos = soup_1.find_all(class_ = 'andes-table__column--value')

    infos_clean = [info.text for info in infos ]


    #Procurar o Numero de peça
    index_search = 0

    part_Number = ''
    while index_search != (len(heads_clean)):
        if heads_clean[index_search] == 'Número de peça':
            part_Number = infos_clean[index_search]
        
        index_search = index_search + 1


    #juntar as heads com as infos
    informacoes = ''
    index = 0
    for h in heads_clean:
        conct = heads_clean[index] + ': ' + infos_clean[index] + ', '
        #Isso aqui foi improvisação total kkkk
        informacoes = informacoes + conct
        index = index + 1
            

    imagens = soup_1.find_all(class_ = 'ui-pdp-image ui-pdp-gallery__figure__image')
    imagens_clean = [imagem.get('data-zoom') for imagem in imagens]


    nomes_clean[0] = retirarBarra(nomes_clean[0])
    part_Number = retirarBarra(part_Number)


    print(part_Number)

    if part_Number == '':
        nome_da_pasta = "Imagens/{}_{}".format(nomes_clean[0],preco) 
    else:
        nome_da_pasta = "Imagens/{} - {}_{}".format(part_Number, nomes_clean[0], preco) 
      
        

                          
                           
    pasta = Path(nome_da_pasta)
    pasta.mkdir()      

    index_imagens = 0

    print(imagens_clean)
    print(len(imagens_clean))


    while index_imagens < (len(imagens_clean)):
        print("T0")
        url = imagens_clean[index_imagens]

        try:
            # Baixa a imagem e salva no arquivo local

            if part_Number == '':
                urllib.request.urlretrieve(url, "Imagens/{}_{}/{}.jpg".format(nomes_clean[0],preco,index_imagens))
                print("T1")
            else:
                urllib.request.urlretrieve(url, "Imagens/{} - {}_{}/{}.jpg".format(part_Number, nomes_clean[0],preco,index_imagens))
                print("T2")

            print("Imagem baixada e salva com sucesso.")
        except Exception as e:

            print("Falha ao baixar a imagem:", str(e))
        
        
            
        index_imagens = index_imagens + 1




    dadoGeral =  part_Number + ";" + nomes_clean[0] + ";" + preco + ";" + pecaAtual + ";" + informacoes + ";" + imagens_clean[0] + '\n'

    with open(nomeArquivo, 'a', encoding ='utf-8')as arquivo:
        arquivo.write(dadoGeral)



def processoInicial(linkPadrao):

    print(linkPadrao)
    print(type(linkPadrao))
    print("\n")


    # Etapa 1
    # Identificar os links da pagina individual de cada peça


    #print("Nome do produto: ")
    #produtoAlvo = input()

    nomeArquivo = "saidaScrapping_bmw-shop_teste.txt"
    #link = linkPadrao + produtoAlvo

    cabecalho = "Número;Nome;Preço;Link;Informações;Imagem\n"

    with open(nomeArquivo, 'w', encoding ='utf-8') as arquivo:
        arquivo.write(cabecalho)

    linkPadrao = "https://loja.mercadolivre.com.br/jeep"

    page = requests.get(linkPadrao)

    soup = BeautifulSoup(page.text, 'html.parser')

    linksObtidos = soup.find_all('a', class_ = 'ui-search-item__group__element ui-search-link')

    linksObtidos_clean = [link.get('href') for link in linksObtidos]#Jogar os links identificados no html em um array

    number_of_pages = 1
    atual = 49

    while(number_of_pages<2):
        number_of_pages = number_of_pages + 1
        link_pgs_seguintes = "https://lista.mercadolivre.com.br/_Desde_{}_Loja_bmw-shop_NoIndex_True".format(atual)
        print(link_pgs_seguintes)
        page = requests.get(link_pgs_seguintes)
        soup = BeautifulSoup(page.text, 'html.parser')
        linksObtidos_2 = soup.find_all('a', class_ = 'ui-search-item__group__element ui-search-link')
        linksObtidos_clean_2 = [link.get('href') for link in linksObtidos_2]#Jogar os links identificados no html em um array
        linksObtidos_clean = linksObtidos_clean + linksObtidos_clean_2
        atual = atual + 48

    # Etapa 2
    # Inicar o scrapping dos dados das peças obtidas

    for pecaAtual in linksObtidos_clean:
        scraping(pecaAtual, nomeArquivo)

    print("Processo Finalizado")

