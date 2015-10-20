from selenium import webdriver


class Injector():

#Creamos las reglas para el webdriver
    def __init__(self):
        self.driver = webdriver.firefox.FirefoxDriver
        #Espera por defecto 10 segundos, a menos que se especifique de otra manera
        self.driver.implicitly_wait(10)

    def inject_driver(self):
        return self.driver