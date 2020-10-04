import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-txt'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

listaLeituras = soup.find_all('table')

url = 'https://firms.modaps.eosdis.nasa.gov'
for lista_td in listaLeituras:
    lista = lista_td.find_all('a')
    for listaDados in lista:
        if listaDados.name == 'a':
            filtro = 'J1_VIIRS_C2_South_America_24h.csv'
            if filtro in listaDados.get('href'):
                url_it = '{0}{1}'.format(url, listaDados.get('href'))
                
urllib.request.urlretrieve(url_it, 'Dados.csv')