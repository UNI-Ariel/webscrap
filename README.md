# Prototipo Inicial Web Scraping con Python
Se realizo el prototipo inicial explorando las estructuras de los sitios web, primero en un navegador, luego utilizando BeautifulSoup para armar una estructura inicial de los elementos que se va a recolectar y despues la obtención.

## Versión de Python
Utilizada es la version 3.13.5

## Instalación de dependencias
`pip install -r requirements.txt`

## Sitios web de referencia
https://compucenter.store/category/2-almacenamiento/9-disco-duro

https://www.dismac.com.bo/tu-real-en-black-friday/categoria_filter_audiomenor-categoria_filter_computacion-categoria_filter_hogarinteligente-categoria_filter_oficina-categoria_filter_telefonia-categoria_filter_videojuegos.html

## Proceso

### Descarga de la página
Se realizo una descarga inicial de las paginas para explorar los elementos sin depender de una conexión en linea.

### Servir las páginas
Iniciar un servidor en python con

`python -m http.server 8080`

Y dirigirse a un navegador web para realizar la exploración de las paginas.

### Exploración con BeautifulSoup
 En el código, armar la estructura de los elementos utilizando los selectores para obtener la información.

### Mostrar resultados
A la ejecución de los scripts los resultados se muestran por consola y como documento, en un archivo ipynb (Jupyter Notebook).
