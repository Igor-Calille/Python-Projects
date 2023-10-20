from bs4 import BeautifulSoup
import requests
import time




def scraping(pecaAtual, nomeArquivo):
    pagePeca = requests.get(pecaAtual)
    soup_1 = BeautifulSoup(pagePeca.text, 'html.parser')

    nomes = soup_1.find_all(class_ = 'ui-pdp-title')
    nomes_clean = [nome.text for nome in nomes]

    preco_null = []
    
    precos = soup_1.find_all(class_= 'andes-money-amount__fraction')
    precos_clean = [preco.text for preco in precos]
    preco = precos_clean[0]
    cents = soup_1.find_all( class_ = 'andes-money-amount__cents andes-money-amount__cents--superscript-36')

    cents_clean = [cent.text for cent in cents]

    if cents_clean != preco_null:
        preco = preco + ',' + cents_clean[0]


    sales = soup_1.find_all( class_ = 'andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact')
    sales_clean = [sale.get('content') for sale in sales ]
    #cents_sales = soup_1.find_all( class_ = 'andes-money-amount__cents andes-money-amount__cents--superscript-36')
    #cents_sales_clean = [cent_sale.text for cent_sale in cents_sales]
    
    sale = ''
    #if  cents_sales_clean != preco_null:
    #   sale = ' -> ' + sales_clean[1] + ',' + cents_sales_clean[1]



    heads = soup_1.find_all(class_ = 'andes-table__header__container')
    heads_clean = [head.text for head in heads ]


    infos = soup_1.find_all(class_ = 'andes-table__column--value')
    infos_clean = [info.text for info in infos ]

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

    dadoGeral =  nomes_clean[0] + ";" + preco + sale + ";" + pecaAtual + ";" + informacoes + ";" + imagens_clean[0] + '\n'

    with open(nomeArquivo, 'a', encoding ='utf-8')as arquivo:
        arquivo.write(dadoGeral)



# Etapa 1
# Identificar os links da pagina individual de cada peça


#print("Nome do produto: ")
#produtoAlvo = input()

nomeArquivo = "saidaScrapping_bmw-shop.txt"
#link = linkPadrao + produtoAlvo

cabecalho = "Nome;Preço;Link;Informações;Imagem\n"

with open(nomeArquivo, 'w', encoding ='utf-8') as arquivo:
    arquivo.write(cabecalho)

linkPadrao = "https://loja.mercadolivre.com.br/bmw-shop"

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

