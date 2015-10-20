from pageobjects.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class HomePage(BasePage):

    def show_title(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is('Pasa la Gorra - Un Techo')
        )
        return self.driver.title