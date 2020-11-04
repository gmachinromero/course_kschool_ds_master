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
class Opinion(Item):
  titulo = Field()
  calificacion = Field()
  contenido = Field()
  autor = Field()


 Clase CrawlSpider - Se define el comportamiento de la araña
# ---------------------------------------------------------------------------------------------------------------
class TripAdvisorSpider_v2(CrawlSpider):
    name = "TripAdvisorSpider_v2"

    # Custom settings
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'CLOSESPIDER_PAGECOUNT': 100}
    
    # URLs
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    # Delay
    download_delay = 1

    # Reglas de crawling (tupla)
    rules = (
         # hztl: paginación hoteles
        Rule(LinkExtractor(allow = r'-oa\d+-'),                     # '\d+': dígitos en RegEx
                           follow = True),     
         # vert: detalle hoteles
        Rule(LinkExtractor(allow = r'/Hotel_Review-'),
                           restrict_xpaths=['//div[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]'],
                           follow = True),
         # hztl: paginación opiniones
        Rule(LinkExtractor(allow = r'-or\d+-'),
                           follow = True), 
         # vert: usuario opinión