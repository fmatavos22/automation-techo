from pageobjects.base import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests, json


class RegisterPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def delete_user(self):
        endpoint_delete_user = "http://172.17.201.128/api/persons/megamanplg001%40mailinator.com"
        requests.delete(endpoint_delete_user)

    def show_title(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is('Registrate en Pasa la Gorra - Un Techo')
        )
        return self.driver.title

    def show_successful_register_title(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is('Registracion Correcta en Pasa la Gorra - Un Techo')
        )

    def do_register(self, name, surname, city, province, country, telephone, email, password):
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[1]/div/input').send_keys(name)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[2]/div/input').send_keys(surname)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[3]/div/input').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[4]/div/input').send_keys(province)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[5]/div/input').send_keys(country)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[6]/div/input').send_keys(telephone)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[7]/div/input').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[8]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="form-wrapper"]/form/div[9]/button').click()

    def quit_browser(self):
        self.driver.quit()