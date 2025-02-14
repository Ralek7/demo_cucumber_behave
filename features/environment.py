from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
