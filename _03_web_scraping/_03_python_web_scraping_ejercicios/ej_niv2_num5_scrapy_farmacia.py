# Importamos librerías de trabajo
# ------------------------------------------------------------------------------
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


# Datos a completar - Determina los datos que tengo que completar, y que se
# encontrarán en el fichero generado
# ------------------------------------------------------------------------------
class Farmacia(Item):
    Nombre = Field()
    Precio = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ------------------------------------------------------------------------------
class CruzVerdeSpider(CrawlSpider):
    name = 'CruzVerdeSpider'

    # Custom settings
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
    
    # URLs
    allowed_domains = ["cruzverde.cl"]
    start_urls = ["https://www.cruzverde.cl/medicamentos/"]

    # Delay
    download_delay = 1

    # Reglas de crawling (tupla)
    rules = (
        Rule(LinkExtractor(allow = r'start=', 
                           tags = ('a', 'button'), 
                           attrs = ('href', 'data-url')),
            follow = True,
            callback = "parse_farmacia"),
    )

    # Parseo de URLs
    def parse_farmacia(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Selector del contenedor productos
        productos = sel.xpath('//div[@class="col-12 col-lg-4"]')
        # Selector de cada producto, y sus atributos
        for producto in productos:
            item = ItemLoader(Farmacia(), producto)
            item.add_xpath('Nombre', './/div[@class="tile-body px-3 pt-3 pb-0 d-flex flex-column pb-0"]//div[@class="pdp-link"]/a/text()')
            item.add_xpath('Precio', './/span[contains(@class, "value ")]/text()')
 
            yield item.load_item()