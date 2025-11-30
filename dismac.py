# %%
from bs4 import BeautifulSoup
import requests

# Obtener el contenido de la pagina
# Esta pagina necesita establecer el encoding a utf-8
res =  requests.get("http://localhost:8080/html/Tu%20real%20en%20black%20friday%20_%20Dismac.html")
res.encoding = "UTF-8"
page = res.text
soup = BeautifulSoup(page, "lxml")

# Mostrar el contenido
str(soup)[:500]

# %%
# Realizar la exploración de la pagina y armar estructura
# El elemento de interes se encuentra en un div con clase "product-item-pdc"
items = soup.find_all("div", {"class": "product-item-pdc"})

# Mostrar los itms
str(items)[:500]

# %%
# El nombre del producto esta en un div con clase "width-section-name"
# E internamente dentro un span con class "name"
for prod in items:
  p = prod.find("span", {"class": "name"})
  print(p)


# %%
# Los precios se encuentran en un div con clase "section-widget-price"
# E internamente en un span con clase "current-price"
for prod in items:
  p = prod.find("span", {"class": "current-price"})
  print(p)

# %%
# Finalmente los datos de interes son
datos = dict()
for prod in items:
  titulo = prod.find("span", {"class": "name"}).text
  precio = prod.find("span", {"class": "current-price"}).text
  print(f"titulo: {titulo}, precio: {precio}")
