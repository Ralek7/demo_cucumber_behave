# pages/savings_investments_page.py
from selenium.webdriver.common.by import By
from utils.element_utils import ElementUtils
from selenium.webdriver.common.action_chains import ActionChains
import time


class SavingsAndInvestmentsPage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = ElementUtils(driver)
        
        # Locators
        self.close_popup = (By.XPATH, "(//button[contains(@aria-label,'Close')])[2]")
        self.ahorro_btn = (By.XPATH, "//span[contains(.,'Ahorro e Inversiones')]")
        self.inversion_creciente_btn = (By.XPATH, "(//a[contains(.,'Inversión Creciente')])[1]")
        self.simulador_btn = (By.XPATH, "//*[@id='contenido']/div[1]/ul/li[4]/a")
        self.monto_input = (By.XPATH, "//*[@id='cantidadInvertir']")
        self.calcular_btn = (By.XPATH, "//*[@id='btn_calcular']/img")
        self.result_text = (By.XPATH, "//*[@id='montoFinalRes']")
        self.access_denied = (By.CLASS_NAME, "error-title")
        self.iframe_id = "main-iframe"

    def check_and_reload(self, max_attempts):
        self.utils.check_and_reload_if_access_denied(self.access_denied, self.iframe_id, max_attempts)

    def click_close_popup(self):
        self.utils.click_element(self.close_popup)

    def click_ahorro(self):
        self.utils.click_element(self.ahorro_btn)

    def click_inversion_creciente(self):
        self.utils.click_element(self.inversion_creciente_btn)

    def click_simulador(self):
        self.utils.click_element(self.simulador_btn)

    def enter_monto(self, monto):
        element = self.utils.wait_for_element(self.monto_input)
        self.utils.scroll_to_element(element)
        self.utils.send_text(self.monto_input, monto)

    def click_calcular(self):
        # self.utils.force_click_with_retry(self.calcular_btn)
        self.utils.click_element(self.calcular_btn)
        time.sleep(1)
        self.utils.click_element(self.calcular_btn)

    def get_result(self):
        element = self.utils.wait_for_element(self.result_text)
        self.utils.scroll_to_element(element)
        return element.text
