# Importamos librerías de trabajo
# ---------------------------------------------------------------------------------------------------------------
from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


# Datos a extraer - Determina los datos que tengo que completar, y que se encontrarán en el fichero generado
# ---------------------------------------------------------------------------------------------------------------
class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()
    
# Clase Spider - Se define el comportamiento
# ---------------------------------------------------------------------------------------------------------------
class StackOverflowSpider(Spider):
    name = "StackOverflowSpider"
    
    # User-Agent
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # URL semilla
    start_urls = ['https://stackoverflow.com/questions']
    
    # Funcion a la que se va a llamar, cuando se haga el requerimiento a la URL semilla
    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Selector de todas las preguntas de la página principal de StackOverflow
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        # Para cada pregunta:
        i = 1
        for pregunta in preguntas:
            # Instanciamos el ítem Pregunta, e indicamos en que variable puede encontrar la información
            item = ItemLoader(Pregunta(), pregunta)
            # Lleno los atributos del ítem Pregunta
            item.add_value('id', i)
            item.add_xpath('pregunta', './/h3/a/text()')                         # El punto del XPath indica ruta relativa
            item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')     # El punto del XPath indica ruta relativa
            i += 1
            # Hago Yield de la informacion para que se escriban los datos del ítem Pregunta, en un archivo
            yield item.load_item()