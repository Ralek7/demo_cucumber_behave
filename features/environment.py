from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Importar el manager

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Recomendado para CI
    
    # Configurar Chrome con el driver automático
    context.driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options
    )

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):  # Verificar si el driver existe
        context.driver.quit()
