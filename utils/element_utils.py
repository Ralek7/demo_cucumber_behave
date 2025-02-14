# utils/element_utils.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
import time

class ElementUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ------------------------- Manejo de Access Denied en iframe -------------------------
    def check_and_reload_if_access_denied(self, access_denied_locator: tuple, iframe_id: str, max_attempts: int):
        attempts = 0
        while attempts < max_attempts:
            try:
                # Cambiar al iframe
                self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_id)))
                
                # Verificar mensaje de error
                if EC.presence_of_element_located(access_denied_locator)(self.driver):
                    print("Access denied detectado. Recargando página...")
                    self.driver.refresh()
                    attempts += 1
            except Exception:
                break
            finally:
                self.driver.switch_to.default_content()
        
        if attempts == max_attempts:
            print("Máximos intentos alcanzados. Access denied persiste.")

    # ------------------------- Esperas y Elementos Básicos -------------------------
    def wait_for_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ------------------------- Efectos Visuales -------------------------
    def highlight_element(self, element: WebElement):
        try:
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        except WebDriverException:
            print("No se pudo resaltar el elemento")

    def unhighlight_element(self, element: WebElement):
        try:
            self.driver.execute_script("arguments[0].style.border=''", element)
        except WebDriverException:
            print("No se pudo quitar el resaltado")

    # ------------------------- Interacciones Básicas -------------------------
    def click_element(self, locator: tuple):
        element = None
        try:
            element = self.wait_for_element_to_be_clickable(locator)
            self.highlight_element(element)
            ActionChains(self.driver).move_to_element(element).click().perform()
        except Exception as e:
            print(f"Error al hacer clic en {locator}: {str(e)}")
            raise
        finally:
            if element:
                self.unhighlight_element(element)

    def send_text(self, locator: tuple, text: str):
        try:
            element = self.wait_for_element(locator)
            self.scroll_to_element(element)
            self.highlight_element(element)
            element.clear()
            element.send_keys(text)
            self.unhighlight_element(element)
        except TimeoutException:
            print(f"Campo no encontrado: {locator}")

    # ------------------------- Manejo de Dropdowns -------------------------
    def select_from_dropdown(self, locator: tuple, visible_text: str):
        try:
            dropdown = self.wait_for_element(locator)
            self.highlight_element(dropdown)
            dropdown.send_keys(visible_text)
            self.unhighlight_element(dropdown)
        except TimeoutException:
            print(f"Dropdown no encontrado: {locator}")

    # ------------------------- Scrolls -------------------------
    def scroll_to_element(self, element: WebElement):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        except WebDriverException:
            print("Error al hacer scroll")

    def scroll_to_element_top(self, element: WebElement):
        try:
            self.driver.execute_script(
                "window.scrollTo(0, arguments[0].getBoundingClientRect().top);", 
                element
            )
        except WebDriverException:
            print("Error al desplazar a la parte superior")
