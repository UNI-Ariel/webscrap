# Prototipo Inicial Web Scraping con Python
Se realizo el prototipo inicial explorando la estructura del sitio web, primero en un navegador, luego utilizando BeautifulSoup para armar una estructura inicial de los elementos que se va a recolectar y despues la obtención

## Versión de Python
Utilizada es la version 3.13.5

## Instalación de dependencias
`pip install -r requirements.txt`

## Sitio web de referencia
https://compucenter.store/category/2-almacenamiento/9-disco-duro

## Proceso

### Descarga de la página
Una única descarga inicial del una sola pagina para explorar los elementos

### Servir la página
Iniciar un servidor en python con

`python -m http.server 8080`

Y dirigirse a *http://localhost:8080/Almacenamiento%20_%20CompuCenter%20Bolivia.html* para realizar la exploración 

### Exploración con BeautifulSoup
 En el código, armar la estructura de los elementos utilizando los selectores para obtener la información

### Mostrar resultados
Por consola y como documentación en un HTML
