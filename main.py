import pandas
import requests
from bs4 import BeautifulSoup

titulos=[]
precios=[]
disponibilidad=[]


url='https://books.toscrape.com/'

r=requests.get(url)
c=r.content
soup=BeautifulSoup(c,'html.parser')
#print(soup.prettify)

articulos=soup.find_all('article',{'class':'product_pod'})

for articulo in articulos:
    elementos_h3=articulo.find('h3')
    titulo = elementos_h3.find('a').get_text()
    precio=articulo.find('p',{'class':'price_color'}).get_text().replace('£','')
    stock=articulo.find('p',{'class':'instock'}).get_text().strip()

    titulos.append(titulo)
    precios.append(precio)
    disponibilidad.append(stock)

datos={
    'TITULO':titulos,
    'PRECIO':precios,
    'DISPONIBILIDAD':disponibilidad
}

df=pandas.DataFrame(datos)
df.to_csv('datos.csv')