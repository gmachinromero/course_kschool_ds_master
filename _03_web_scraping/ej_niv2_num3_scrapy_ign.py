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
    titulo_art = Field()
    contenido = Field()

class Review(Item):
    titulo_rev = Field()
    calificacion = Field()

class Video(Item):
    titulo_vid = Field()
    fecha_de_publicacion = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class IgnCrawler(CrawlSpider):
    name = "IgnCrawler"

    # Custom settings
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'CLOSESPIDER_PAGECOUNT': 30} # Control del número de URLs parseadas

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['latam.ign.com']

    # URL semilla
    start_urls = ['https://latam.ign.com/se/?model=article&q=ps4']

    # Programamos un delay (segundos) para evitar ser baneados
    download_delay = 1

    # Reglas de crawling (tupla)
    rules = (
        Rule(LinkExtractor(allow = r'/type='), follow = True),                                # horizontal: tipo
        Rule(LinkExtractor(allow = r'/&page='), follow = True),                               # horizontal: paginación
        Rule(LinkExtractor(allow = r'/news/'), follow = True, callback = 'parse_articulo'),   # vertical: Articulos
        Rule(LinkExtractor(allow = r'/review/'), follow = True, callback = 'parse_review'),   # vertical: Reviews
        Rule(LinkExtractor(allow = r'/video/'), follow = True, callback = 'parse_video'),)    # vertical: Videos


    # Función de limpieza de los campos descriptivos (se puede sustituir por una lambda como argumento del MapCompose())
    def text_cleaning(self, text):
        clean_text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return clean_text


    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla. Esta función se ejecuta
    # en cada link que cumpla las reglas definidas en la tupla rules

    # Artículo
    def parse_articulo(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo_art', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('contenido', '//div[@id="id_text"]//*/text()', MapCompose(self.text_cleaning))
        yield item.load_item()

    # Review
    def parse_review(self, response):
        item = ItemLoader(Review(), response)
        item.add_xpath('titulo_rev', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('calificacion', '//span[@class="side-wrapper side-wrapper hexagon-content"]/text()', MapCompose(self.text_cleaning))
        yield item.load_item()

    # Video
    def parse_video(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo_vid', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()', MapCompose(self.text_cleaning))
        yield item.load_item()


# Ejecución
# ---------------------------------------------------------------------------------------------------------------
# scrapy runspider ej_niv2_num3_scrapy_ign.py -o ej_niv2_num3_scrapy_ign.json