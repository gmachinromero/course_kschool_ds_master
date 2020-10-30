# Importamos librerías de trabajo
from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# Datos a extraer - Determina los datos que tengo que completar, y que se encontrarán en el fichero generado
class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()
    
# Clase Spider - Se define el comportamiento
class StackOverflowSpider(Spider):
    name = "StackOverflowSpider"
    
    # User-Agent
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    
    # URL semilla
    start_urls = ['https://stackoverflow.com/questions']
    
    # Funcion que se va a llamar cuando se haga el requerimiento a la URL semilla
    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)
        # Selector del título de la página
        titulo_de_pagina = sel.xpath('//h1/text()').get()
        # Selector de varias preguntas
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="question-summary"]')
        # Para cada pregunta:
        i = 0
        for pregunta in preguntas:
            # Instancio mi ítem con el selector en donde están los datos para llenarlo
            item = ItemLoader(Pregunta(), pregunta)
            # Lleno los atributos de mi ítem
            item.add_value('id', i)
            item.add_xpath('pregunta', './/h3/a/text()') 
            item.add_xpath('descripcion', './/div[@class="excerpt"]/text()')
            i += 1
            # Hago Yield de la informacion para que se escriban los datos en el archivo
            yield item.load_item()