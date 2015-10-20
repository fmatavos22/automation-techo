import unittest
import webdriver.web_driver_helper
from pageobjects.login import LoginPage
from pageobjects.home import HomePage
from pageobjects.register import RegisterPage


class Login(unittest.TestCase):

    def setUp(self):
        self.starter = webdriver.web_driver_helper.Injector()
        self.login_page = LoginPage(self.starter.inject_driver())
        self.login_page.open('http://172.17.201.128/#/login')

    def test_login_is_available(self):
        assert self.login_page.show_title() == 'Login'

    def test_successful_login(self):
        self.login_page.do_login('federico.matavos@globallogic.com', 'password')
        home_page = HomePage(self.starter.inject_driver())
        assert home_page.show_title() == 'Pasa la Gorra - Un Techo'

    #Agregar busquedas de elementos basicos de la home

    def test_failed_login(self):
        self.login_page.do_login('sarasa', 'sarasa1234')
        assert self.login_page.show_error() == 'Las credenciales son inválidas'

    def test_register_click(self):
        self.login_page.click_register()
        register_page = RegisterPage(self.starter.inject_driver())
        assert register_page.show_title() == 'Registrate en Pasa la Gorra - Un Techo'

    def tearDown(self):
        self.login_page.quit_browser()