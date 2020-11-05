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
class Opinion(Item):
  titulo = Field()
  calificacion = Field()
  contenido = Field()
  autor = Field()


# Clase CrawlSpider - Se define el comportamiento de la araña
# ------------------------------------------------------------------------------
class TripAdvisorSpider_v2(CrawlSpider):
    name = "TripAdvisorSpider_v2"

    # Custom settings
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 50
        }
    
    # URLs
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Hotels-g303845-Guayaquil_Guayas_Province-Hotels.html']

    # Delay
    download_delay = 0.5


    # Reglas de crawling (tupla)
    rules = (
         # hztl: paginación hoteles
        Rule(LinkExtractor(allow = r'-oa\d+-'),
                           follow = True),     
         # vert: detalle hoteles
        Rule(LinkExtractor(allow = r'/Hotel_Review-',
                           restrict_xpaths=['//div[@id="taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_0"]']),
                           follow = True),
         # hztl: paginación opiniones
        Rule(LinkExtractor(allow = r'-or\d+-'),
                           follow = True), 
         # vert: usuario opinión
         Rule(LinkExtractor(allow = r'/Profile/',
                            restrict_xpaths=['//div[@data-test-target="reviews-tab"]']),
                            follow = True,
                            callback = 'parse_opinion'),
    )
    

    # Función de limpieza de los campos descriptivos (se puede sustituir por una
    # lambda como argumento del MapCompose())
    def text_cleaning(self, text):
        clean_text = text.replace('\n', '').replace('\r', '').replace('\t', '').strip()
        return clean_text


    # Parseo de URLs
    def parse_opinion(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Selector del autor
        autor = sel.xpath('//h1/span/text()').get()
        # Selector de todas las opiniones de un perfil
        opiniones = sel.xpath('//div[@id="content"]/div/div')
        for opinion in opiniones:
            item = ItemLoader(Opinion(), opinion)
            item.add_value('autor', autor)
            item.add_xpath('titulo', './/div[contains(@class, "_3IEJ3tAK")]/text()', MapCompose(self.text_cleaning))
            item.add_xpath('calificacion', './/div[contains(@class, "_1VhUEi8g")]//span[contains(@class, "ui_bubble_rating")]/@class', MapCompose(lambda i: i.split('_')[-1]))
            item.add_xpath('contenido', './/q/text()', MapCompose(self.text_cleaning))

            yield item.load_item()



# Ejecución
# ------------------------------------------------------------------------------
# scrapy runspider ej_niv2_num4_scrapy_tripadvisor.py -o ej_niv2_num4_scrapy_tripadvisor.json