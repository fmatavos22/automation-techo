import unittest
import webdriver.web_driver_helper
from pageobjects.register import RegisterPage


class Register(unittest.TestCase):

    def setUp(self):
        self.starter = webdriver.web_driver_helper.Injector()
        self.register_page = RegisterPage(self.starter.inject_driver())
        self.register_page.open('http://172.17.201.128/#/registracion')

    def test_register_is_available(self):
        assert self.register_page.show_base_title() == 'Registrate en Pasa la Gorra - Un Techo'

    def test_successful_register(self):
        self.register_page.do_register('Mega', 'Man', 'Capital', 'Robotnia', 'Robot', '01010101', 'megamanplg001@mailinator.com', 'password')
        assert self.register_page.show_successful_register_title() == 'Registracion Correcta en Pasa la Gorra - Un Techo'

    #def tearDown(self):
       # self.register_page.quit_browser()