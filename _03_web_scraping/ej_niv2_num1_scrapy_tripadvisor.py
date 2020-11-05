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
class Hotel(Item):
    nombre = Field()
    descripcion = Field()
    servicios = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class TripAdvisorSpider(CrawlSpider):
    name = "TripAdvisorSpider"
    
    # Custom settings
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ['tripadvisor.com']

    # URL semilla
    start_urls = ['https://www.tripadvisor.com/Hotels-g187514-Madrid-Hotels.html']

    # Programamos un delay (segundos) para evitar ser baneados
    download_delay = 1

    # Definimos a que URLs dentro de la URL semilla tiene que ir o no la CrawlSpider. En este caso, la araña se
    # va a obtener todos aquellos links de la URL semilla que contengan el string '/Hotel_Review-g187514-' y en 
    # cada uno de ellos se ejecutará la función de parseo
    rules = (Rule(LinkExtractor(allow = r'/Hotel_Review-g187514-'), follow = True, callback = 'parse_item'),) # r es de RegEx

    # Función de limpieza de los campos descriptivos (se puede sustituir por una lambda como argumento del MapCompose())
    def data_cleaning(self, text):
        clean_text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        return clean_text

    # Funcion para diseccionar (parse) la respuesta de la solicitud a la URL semilla. Esta función se ejecuta
    # en cada link que cumpla las reglas definidas en la tupla rules
    def parse_item(self, response):

        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)

        # Instanciamos el ítem Hotel, e indicamos en que variables puede encontrar la información
        item = ItemLoader(Hotel(), sel)

        # Completo los atributos del ítem Hotel
        item.add_xpath('nombre',
                       '//h1[@id="HEADING"]/text()')
        item.add_xpath('descripcion',
                       '//div[contains(@class, "_2-hMril5")]//div[contains(@class, "cPQsENeY")]/text()',
                       MapCompose(self.data_cleaning))
        item.add_xpath('servicios',
                       '//div[contains(@class, "_1nAmDotd")][1]//div[contains(@class, "_2rdvbNSg")]/text()')

        # Hago Yield de la informacion para que se escriban los datos del ítem Hotel, en un archivo
        yield item.load_item()


# Ejecución
# ---------------------------------------------------------------------------------------------------------------
# scrapy runspider ej_niv2_num1_scrapy_tripadvisor.py -o ej_niv2_num1_scrapy_tripadvisor.json