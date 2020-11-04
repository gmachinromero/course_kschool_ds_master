# Importamos librerías de trabajo
# ---------------------------------------------------------------------------------------------------------------
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


# Datos a completar - Determina los datos que tengo que completar, y que se encontrarán en el fichero generado
# ---------------------------------------------------------------------------------------------------------------
class Articulo(Item):
    titulo = Field()
    contenido = Field()

class Review(Item):
    titulo = Field()
    calificacion = Field()

class Video(Item):
    titulo = Field()
    fecha_de_publicacion = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class IgnCrawler(CrawlSpider):
    name = "IgnCrawler"

    # Custom settings
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'CLOSESPIDER_PAGECOUNT': 20} # Control del número de URLs parseadas

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['latam.ign.com']

    # URL semilla
    start_urls = ['https://latam.ign.com/se/?model=article&q=ps4']

    # Programamos un delay (segundos) para evitar ser baneados
    download_delay = 1

    # Reglas de crawling (tupla)
    rules = (
        # crawling horizontal por tipo
        Rule(LinkExtractor(allow = r'/type='), follow = True),
        # crawling horizontal por número de página dentro de cada tipo
        Rule(LinkExtractor(allow = r'/&page='), follow = True),
        # crawling vertical: Articulos
        Rule(LinkExtractor(allow = r'/news/'), follow = True, callback = 'parse_articulo'),
        # crawling vertical: Reviews
        Rule(LinkExtractor(allow = r'/review/'), follow = True, callback = 'parse_review'),
        # crawling vertical: Videos
        Rule(LinkExtractor(allow = r'/video/'), follow = True, callback = 'parse_video'),)

    # Función de limpieza de los campos descriptivos (se puede sustituir por una lambda como argumento del MapCompose())
    def text_cleaning(self, text):
        clean_text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return clean_text


    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla. Esta función se ejecuta
    # en cada link que cumpla las reglas definidas en la tupla rules
    def parse_articulo(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Instanciamos el ítem Articulo, e indicamos en que variables puede encontrar la información
        item = ItemLoader(Articulo(), sel)
         # Completo los atributos del ítem Articulo
        item.add_xpath('titulo', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('contenido', '//span[@class="side-wrapper side-wrapper hexagon-content"]/text()', MapCompose(self.text_cleaning))
        # Hago Yield de la informacion para que se escriban los datos del ítem Articulo, en un archivo
        yield item.load_item()

    def parse_review(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Instanciamos el ítem Review, e indicamos en que variables puede encontrar la información
        item = ItemLoader(Review(), sel)
         # Completo los atributos del ítem Review
        item.add_xpath('titulo', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('calificacion', '//div[@id="id_text"]//*/text()', MapCompose(self.text_cleaning))
        # Hago Yield de la informacion para que se escriban los datos del ítem Review, en un archivo
        yield item.load_item()

    def parse_video(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Instanciamos el ítem Video, e indicamos en que variables puede encontrar la información
        item = ItemLoader(Video(), sel)
         # Completo los atributos del ítem Video
        item.add_xpath('titulo', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()', MapCompose(self.text_cleaning))
        # Hago Yield de la informacion para que se escriban los datos del ítem Video, en un archivo
        yield item.load_item()


# Ejecución
# ---------------------------------------------------------------------------------------------------------------
# scrapy runspider ej_niv2_num3_scrapy_ign.py -o ej_niv2_num3_scrapy_ign.json