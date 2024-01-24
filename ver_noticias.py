import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_post=[]

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

posts = site.findAll('div', attrs={'class': 'feed-post-body'})

for post in posts:
    titulo = post.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    subtitulo = post.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})

    if subtitulo:
        lista_post.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_post.append([titulo.text, '', titulo['href']])


noticias = pd.DataFrame(lista_post, columns=['titulo', 'subititulo', 'link'])

print(noticias)
noticias.to_excel('noticias.xlsx', index=False)