from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    # Configurar Chrome
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Opcional
    context.driver = webdriver.Chrome(options=options)

def after_scenario(context, scenario):
    # Cerrar el navegador
    context.driver.quit()