# Importamos librerías de trabajo
# ------------------------------------------------------------------------------
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Definimos el user-agent
# ------------------------------------------------------------------------------
opts = Options()
opts.add_argument(
    "user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    )


# Instancio el driver de Selenium que va a controlar el navegador
# ------------------------------------------------------------------------------
driver = webdriver.Chrome('./chromedriver.exe', options = opts)

# Realizo una solicitud en la URL semilla
driver.get('https://www.olx.com.ec')
driver.refresh()

sleep(5)


# Cargamos más información en la URL mediante el botón
# ------------------------------------------------------------------------------
for i in range(3): # Voy a darle click en "cargar más" 3 veces
    try:
        # busco el botón mediante condiciones esperadas
        boton = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located(
              (By.XPATH, '//button[@data-aut-id="btnLoadMore"]')
              )
        )

        # click
        boton.click()

        # espero que cargue la información dinámica (se puede randomizar)
        WebDriverWait(driver, 10).until(
          EC.presence_of_element_located(
              (By.XPATH, '//li[@data-aut-id="itemBox"]')
              )
        )
    except:
        # si hay algun error, terminamos el bucle
        break


# Realizamos web scraping de la respuesta
# ------------------------------------------------------------------------------
# Defino el XPath de los elementos que quiero extraer
anuncios = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Recorro cada uno de los anuncios que he encontrado
for anuncio in anuncios:

    # Precio
    precio = anuncio.find_element_by_xpath(
        './/span[@data-aut-id="itemPrice"]').text
    print (precio)
    # Descripcion
    descripcion = anuncio.find_element_by_xpath(
        './/span[@data-aut-id="itemTitle"]').text
    print (descripcion)

