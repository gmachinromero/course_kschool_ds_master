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
    precio = Field()
    descripcion = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class MercadoLibreCrawler(CrawlSpider):
    name = "MercadoLibreCrawler"

    # Custom settings
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'CLOSESPIDER_PAGECOUNT': 20} # Control del número de URLs parseadas

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['articulo.mercadolibre.com.ec', 'listado.mercadolibre.com.ec']

    # URL semilla
    start_urls = ['https://listado.mercadolibre.com.ec/animales-mascotas/perros/']

    # Programamos un delay (segundos) para evitar ser baneados
    download_delay = 1

    # Reglas de crawling (tupla)
    rules = (
        # crawling horizontal (paginación)
        Rule(LinkExtractor(allow = r'/_Desde_'), follow = True),
        # crawling vertical (detalle de los productos)
        Rule(LinkExtractor(allow = r'/MEC-'), follow = True, callback = 'parse_item'),)


    # Función de limpieza de los campos descriptivos (se puede sustituir por una lambda como argumento del MapCompose())
    def text_cleaning(self, text):
        clean_text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return clean_text

    
    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla. Esta función se ejecuta
    # en cada link que cumpla las reglas definidas en la tupla rules
    def parse_item(self, response):

        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)

        # Instanciamos el ítem Articulo, e indicamos en que variables puede encontrar la información
        item = ItemLoader(Articulo(), sel)

         # Completo los atributos del ítem Articulo
        item.add_xpath('titulo', '//h1/text()', MapCompose(self.text_cleaning))
        item.add_xpath('precio', '//span[@class = "price-tag-fraction"]/text()', MapCompose(self.text_cleaning))
        item.add_xpath('descripcion', '//div[@class = "item-description__text"]/p/text()', MapCompose(self.text_cleaning))


        # Hago Yield de la informacion para que se escriban los datos del ítem Hotel, en un archivo
        yield item.load_item()


# Ejecución
# ---------------------------------------------------------------------------------------------------------------
# scrapy runspider ej_niv2_num2_scrapy_mercadolibre.py -o ej_niv2_num2_scrapy_mercadolibre.json