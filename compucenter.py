# %%
from bs4 import BeautifulSoup
import requests

# Obtener el contenido de la pagina
page = requests.get("http://localhost:8080/Almacenamiento%20_%20CompuCenter%20Bolivia.html").text
soup = BeautifulSoup(page, "lxml")

# Mostrar el contenido
soup

# %%
# Realizar la exploración de la pagina y armar estructura
# Inicialmente se encuentra que las ofertas estan en un elemento "article"
ventas = soup.find_all("article")

# Mostrar las ventas
ventas

# %%
# Nombres y descripción de los productos en h2
# El primer h2 el nombre y el segundo la desc
for prod in ventas:
  p = prod.find_all("h2")
  print(p)

# %%
# Precios
# El segundo span contiene los precios
for prod in ventas:
  p = prod.find_all("span")
  print(p)

# %%
# Visualización de los datos de interes
datos = dict()
for prod in ventas:
  m1 = prod.find_all("h2")
  m2 = prod.find_all("span")
  titulo = m1[0].text
  descripcion = m1[1].text
  precio = m2[1].text
  print(f"titulo: {titulo}, descripcion: {descripcion}, precio: {precio}")
