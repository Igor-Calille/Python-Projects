#ignorar esse arquivo


from bs4 import BeautifulSoup
import requests




def scrapping(pecaAtual):
    pagePeca = requests.get(pecaAtual)
    soup_1 = BeautifulSoup(pagePeca.text, 'html.parser')

    nomes = soup_1.find_all(class_ = 'ui-pdp-title')
    nomes_clean = [nome.text for nome in nomes]

    precos = soup_1.find_all(class_= 'andes-money-amount__fraction')
    precos_clean = [preco.text for preco in precos]

    marcas = soup_1.find_all(class_ = 'andes-table__column--value')
    marcas_clean = [marca.text for marca in marcas ]

    numeroPecas = soup_1.find_all(class_ = 'andes-table__column andes-table__column--left andes-table__column--vertical-align-center ui-vpp-striped-specs__row__column')
    numeroPecas_clean = [numeroPeca.text for numeroPeca in numeroPecas]

    print(nomes_clean)
    print(precos_clean)
    print(marcas_clean)
    print(numeroPecas_clean)

    



# Etapa 1
# Identificar os links da pagina individual de cada peça


linkPadrao = "https://lista.mercadolivre.com.br/válvula torre compressor"

#print("Nome do produto: ")
#produtoAlvo = input()

#link = linkPadrao + produtoAlvo

page = requests.get(linkPadrao)

soup = BeautifulSoup(page.text, 'html.parser')

linksObtidos = soup.find_all('a', class_ = 'ui-search-item__group__element ui-search-link')

linksObtidos_clean = [link.get('href') for link in linksObtidos]#Jogar os links identificados no html em um array
#print(linksObtidos_clean)

# Etapa 2
# Inicar o scrapping dos dados das peças obtidas

for pecaAtual in linksObtidos_clean:
    print(pecaAtual)
    scrapping(pecaAtual)

