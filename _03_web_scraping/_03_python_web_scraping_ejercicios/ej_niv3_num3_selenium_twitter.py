# Importamos librerías de trabajo
# ------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


# Definimos el user-agent
# ------------------------------------------------------------------------------
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")


# Instancio el driver de Selenium que va a controlar el navegador
# ------------------------------------------------------------------------------
driver = webdriver.Chrome('./chromedriver.exe', options = opts)
# Realizo una solicitud en la URL semilla
driver.get('https://twitter.com/login')


# Introduzco credenciales twitter
# ------------------------------------------------------------------------------
user = "machinclothing"
password = "Piedralaves93"


# Web scraping de twitter
# ------------------------------------------------------------------------------
# Obtengo los inputs de usuario y password (son dinámicos)
input_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//input[@name="session[username_or_email]"]')
        )
)
input_pass = driver.find_element(By.XPATH, '//input[@name="session[password]"]')

# Escribo mi usuario input
input_user.send_keys(user)

# Escribo mi contraseña en el input
input_pass.send_keys(password)

# Obtengo el boton de login y le doy click
login_button = driver.find_element(
    By.XPATH,
    '//main//div[@data-testid="LoginForm_Login_Button"]/div[@dir="auto"]'
    )
login_button.click()

# Espero a que aparezcan los tweets
tweets = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//section//article//div[@lang="es"]')
        )
)

# Imprimo el texto de los tweets
for tweet in tweets:
  print(tweet.text)