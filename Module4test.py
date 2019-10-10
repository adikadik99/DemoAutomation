import HtmlTestRunner
from Module4.Driver.DriverChrome import chromedriver
from Module4.Pages.HomeP import HomePage
from Module4.Pages.Register import RegisterPage
from Module4.Pages.Cart import OrderPage
import unittest

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_sign_up(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/")
        driver.implicitly_wait(5)
        homepage = HomePage(driver)
        homepage.click_sign_up()
        driver.implicitly_wait(5)
        rgst = RegisterPage(driver)
        rgst.enter_firstname("Eddie")
        rgst.enter_lastname("Ali")
        rgst.enter_adress("65 Martin Ross")
        rgst.enter_email("eddieali12@gmail.com")
        rgst.enter_phone("4169099494")
        rgst.click_male()
        rgst.click_cricket()
        rgst.select_language()
        rgst.select_skills()
        rgst.select_countries1()
        rgst.select_countries2()
        rgst.select_year()
        rgst.select_month()
        rgst.select_day()
        rgst.enter_password("Eddie99")
        rgst.confirm_password("Eddie99")
        rgst.click_submit()
        driver.implicitly_wait(20)

    def test_weborder(self):
        driver = self.driver
        driver.implicitly_wait(15)
        driver.get("http://practice.automationtesting.in/")
        order = OrderPage(driver)
        order.click_practice_page()
        self.driver.save_screenshot("/Users/adik/PycharmProjects/selenium/Module4/ScreenShot/image.png")
        driver.implicitly_wait(5)
        order.click_add_to_cart()
        order.click_cart()
        order.click_checkout()
        order.enter_firstname("Eddie")
        order.enter_lastname("Ali")
        order.enter_company_name("TF")
        order.enter_email("eddiealie@gmail.com")
        order.enter_phone("4169099494")
        order.select_country()
        order.enter_adress("MartinRoss")
        order.enter_city()
        order.select_province()
        order.enter_postalcode("m3j2l6")
        order.select_payment()
        order.place_order()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output=Reports, verbosity=2)))
