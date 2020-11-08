# Importamos librerías de trabajo
# ------------------------------------------------------------------------------
import random
from time import sleep
from selenium import webdriver


# Instancio el driver de selenium que va a controlar el navegador
# ------------------------------------------------------------------------------
driver = webdriver.Chrome('./chromedriver.exe')

# Realizo una solicitud en la URL semilla
driver.get('https://www.olx.com.ec/autos_c378')
driver.refresh()


# Cargamos más información en la URL mediante el botón
# ------------------------------------------------------------------------------
sleep(5)
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(3): # Voy a darle click en cargar mas 3 veces
    try:
        # click
        boton.click()
        # espero que cargue la informacion
        sleep(random.uniform(8.0, 12.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element_by_xpath(
            '//button[@data-aut-id="btnLoadMore"]')
    except:
        # si hay algun error, terminamos el bucle
        break


# Realizamos web scraping de la respuesta
# ------------------------------------------------------------------------------
# Defino el XPath de los elementos que quiero extraer
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Recorro cada uno de los anuncios que he encontrado
for auto in autos:

    # Precio
    precio = auto.find_element_by_xpath(
        './/span[@data-aut-id="itemPrice"]').text
    print (precio)
    # Descripcion
    descripcion = auto.find_element_by_xpath(
        './/span[@data-aut-id="itemTitle"]').text
    print (descripcion)