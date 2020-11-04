# Importamos librerías de trabajo
# ---------------------------------------------------------------------------------------------------------------
from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


# Datos a completar - Determina los datos que tengo que completar, y que se encontrarán en el fichero generado
# ---------------------------------------------------------------------------------------------------------------
class Noticia(Item):
    titular = Field()
    descripcion = Field()

# Clase Spider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class ElUniversoSpider(Spider):
    name = "ElUniversoSpider"
    
    # User-Agent
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # URL semilla
    start_urls = ['https://www.eluniverso.com/deportes']

    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla
    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Selector de todas las noticias de la sección de deportes de El Universo
        noticias = sel.xpath('//div[@class="view-content"]/div[@class="posts"]')
        # Para cada pregunta:
        for noticia in noticias:
            # Instanciamos el ítem Noticia, e indicamos en que variable puede encontrar la información
            item = ItemLoader(Noticia(), noticia)
            # Completo los atributos del ítem Noticia
            item.add_xpath('titular', './/h2/a/text()')
            item.add_xpath('descripcion', './/p/text()')

            # Hago Yield de la informacion para que se escriban los datos del ítem Noticia, en un archivo
            yield item.load_item()