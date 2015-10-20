__author__ = 'Fede'

from pageobjects.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def open(self, url):
        self.driver.get(url)

#especificacion de wait explicito
    def show_title(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form-wrapper"]/form/div[4]/button'))
        )
        #devuelve el titulo para despues usarlo segun necesitemos
        return self.driver.title

    def show_error(self):
        return self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[4]/span').text

    def do_login(self, user, password):
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[1]/div/input').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[4]/button').click()

    def click_register(self):
        self.driver.find_element_by_xpath('//*[@id="create-account"]').click()

    def quit_browser(self):
        self.driver.quit()