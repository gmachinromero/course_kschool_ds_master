# Importamos librerías de trabajo
# ------------------------------------------------------------------------------
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


# Definimos el user-agent
# ------------------------------------------------------------------------------
opts = Options()
opts.add_argument(
    "user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    )


# Instancio el driver de Selenium que va a controlar el navegador
# ------------------------------------------------------------------------------
driver = webdriver.Chrome('./chromedriver.exe', options = opts)

# Realizo una solicitud en la URL semilla
driver.get(
    'https://www.google.com/maps/place/Restaurante+Amazonico/@40.4237431,-3.6873174,17z/data=!3m1!4b1!4m7!3m6!1s0xd422899dc90366b:0xce28a1dc0f39911d!8m2!3d40.4237431!4d-3.6851287!9m1!1b1'
    )
driver.refresh()

# A veces google places necesita una espera adicional para cargarse
sleep(random.uniform(4.0, 8.0))


# Defino la función scrolling
# ------------------------------------------------------------------------------
def getScrollingScript(iteration):
    # Script de scrolling de javascript.
    scrollingScript = """
      document.getElementsByClassName('section-layout section-scrollbox\
      scrollable-y scrollable-show')[0].scroll(0, 20000)
    """
    return scrollingScript.replace('20000', str(20000 * (iteration + 1)))


# Lógica del scrolling de opiniones
# ------------------------------------------------------------------------------
n_scrolls = 3
SCROLLS = 0
while (SCROLLS != n_scrolls):
  driver.execute_script(getScrollingScript(SCROLLS)) # Ejecuta javascript
  sleep(random.uniform(4, 5))
  SCROLLS += 1


# Realizamos web scraping de la respuesta
# ------------------------------------------------------------------------------

# Contenedor de opiniones
restaurantsReviews = driver.find_elements(
    By.XPATH, '//div[contains(@class, "section-review ripple-container")]'
    )

# Por cada opinión
for review in restaurantsReviews:
    # Obtengo el contenedor del nombre de usuario
    userLink = review.find_element(
        By.XPATH, './/div[@class="section-review-title"]'
        )

    try:
        # Abrimos el perfil del usuario
        userLink.click()
        # Nos movemos a la segunda ventana (perfil usuario)
        driver.switch_to.window(driver.window_handles[1]) # 0 based index

        # Damos click en el tab de opiniones del usuario
        opiniones_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[@class="section-tab-bar-tab \
                    ripple-container section-tab-bar-tab-unselected"]')
                )
            )
        opiniones_tab.click()

        # Contenedor de opiniones
        userReviews = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH, '//div[contains(@class,"section-review \
                        ripple-container")]'))
            )

        # Logica de Scrolling de las opiniones del usuario
        n_scrolls = 3
        USER_SCROLLS = 0
        while (USER_SCROLLS != n_scrolls):
            driver.execute_script(getScrollingScript(USER_SCROLLS))
            sleep(random.uniform(4, 5))
            USER_SCROLLS += 1

        # Obtenemos todos los reviews visibles del usuario
        userReviews = driver.find_elements(
            By.XPATH,'//div[contains(@class,"section-review ripple-container")]'
            )

        # Por cada review que ha hecho el usuario...
        for userReview in userReviews:
            # Obtener la informacion de cada review
            reviewRating = userReview.find_element(
                By.XPATH, './/span[@class="section-review-stars"]'
                ).get_attribute('aria-label')
            userParsedRating = float(
                ''.join(filter(str.isdigit or str.isspace, reviewRating))
                )
            reviewText = userReview.find_element(
                By.XPATH, './/span[@class="section-review-text"]'
                ).text

            print (userParsedRating)
            print (reviewText)

        # Cerramos el tab que se nos abrio
        driver.close()

        # Movemos el contexto del driver al unico tab abierto, el primero
        driver.switch_to.window(driver.window_handles[0])

    # Si ocurre algun error, cierro el tab abierto, y vuelvo al tab original
    except Exception as e:
        print(e)
        driver.close() 
        driver.switch_to.window(driver.window_handles[0])