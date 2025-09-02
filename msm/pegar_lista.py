from bs4 import BeautifulSoup
from numpy import DataSource
import requests



#x = input("Digite o nome do monstro: ")
url = 'https://mysingingmonsters.fandom.com/wiki/kayna'
texto = requests.get(url)
soup = BeautifulSoup(texto.text, 'html.parser')
filtro = soup.find('div', {'data-source': 'wublin inventory'})
monstros = [a.get('title') for a in filtro.find_all('a') if a.get('title')]
quantidade = [sup.get_text() for sup in filtro.find_all('sup') if sup.get_text().isascii]
total = []
for i in range(len(monstros)):
    total.append(monstros[i]+" "+quantidade[i])
print(len(total))
