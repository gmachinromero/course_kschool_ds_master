# Importamos librerías de trabajo
# ---------------------------------------------------------------------------------------------------------------
from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup


# Datos a completar - Determina los datos que tengo que completar, y que se encontrarán en el fichero generado
# ---------------------------------------------------------------------------------------------------------------
class Noticia(Item):
    titular = Field()
    descripcion = Field()

# Clase Spider - Se define el comportamiento de araña
# ---------------------------------------------------------------------------------------------------------------
class ElUniversoSpider(Spider):
    name = "ElUniversoSpider"
    
    # User-Agent
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # URL semilla
    start_urls = ['https://www.eluniverso.com/deportes']

    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla
    def parse(self, response):
        # Soup: Clase de BeautifulSoup para parsear el árbol HTML
        soup = BeautifulSoup(response.body)
        # Selector del contenedor de contenedores de noticias
        contenedor_noticias = soup.find_all('div', class_ = 'view-content')
        #Selector de cada noticia
        for contenedor in contenedor_noticias:
            noticias = contenedor.find_all('div', class_ = 'posts', recursive = False)   # Recursive controla el parseo en hijos directos
            for noticia in noticias:
                # Instanciamos el ítem Noticia, e indicamos en que variables puede encontrar la información
                item = ItemLoader(Noticia(), response.body)
                # Completo los atributos del ítem Noticia
                titular = noticia.find('h2').text
                descripcion = noticia.find('p')             # Existen noticias que no tienen descripcion

                if (descripcion != None):
                    descripcion = descripcion.text
                else:
                    descripcion = 'N/A'

                item.add_value('titular', titular)
                item.add_value('descripcion', descripcion)
                
                # Hago Yield de la informacion para que se escriban los datos del ítem Noticia, en un archivo
                yield item.load_item()