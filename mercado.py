import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'
pesquisa = input("Qual produto você deseja procurar: ")


response = requests.get(url_base + pesquisa)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': "ui-search-result__wrapper"})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
    link = produto.find('a', attrs = {'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    preco = produto.find('div', attrs={'class': 'ui-search-price__second-line'})
    decimais = preco.find('span', attrs={'class': 'andes-money-amount__fraction'})
    centavos = preco. find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

        

    print(titulo.text)
    print(link['href'])
    if centavos:
        print(f'R${decimais.text},{centavos.text}')

    else:
        print(f'R${decimais.text}')
    print()
